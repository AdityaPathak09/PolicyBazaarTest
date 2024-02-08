import datetime
import inspect
import time

import pytest

from PageObjects.HomePage import HomePage
from PageObjects.TermInsurancePage import TermInsurancePage
from Utilities.ReadProperties import ReadConfig
from Utilities.logger import LogGen
from Utilities.XLUtils import *

class Test_TermInsurance:

    Application_URL = ReadConfig.getApplicationURL()


    @pytest.mark.title_check
    @pytest.mark.Term_Insurance
    def test_Term_Insurance_Page_Title(self, setup):
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Page".center(75, "_"))

        self.driver.get(self.Application_URL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        print(f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}")

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance - Buy Best Term Insurance Plan and Policy Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True

        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


    @pytest.mark.Term_Insurance
    @pytest.mark.parameters_check
    def test_term_insurance_list(self, setup):
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Term Insurance List")

        self.driver.get(self.Application_URL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        for indexing in range(4, getRowCount("Term_Life_Insurance_List")+1):

            try:

                life_coverage_amount = readData("Term_Life_Insurance_List", indexing, 1)
                self.terminsurance.select_life_cover_amount(life_coverage_amount)

                coverage_years = readData("Term_Life_Insurance_List", indexing, 2)
                self.terminsurance.select_coverage_till(coverage_years)

                premium_type = readData("Term_Life_Insurance_List", indexing, 3)
                if premium_type == "Yearly":
                    self.terminsurance.press_Yearly_button()
                elif premium_type == "Monthly":
                    self.terminsurance.press_Monthly_button()

                sort_by = readData("Term_Life_Insurance_List", indexing, 5)
                sort_by_type = readData("Term_Life_Insurance_List", indexing, 4)

                if sort_by == "Price":
                    self.terminsurance.sort_by_price(sort_by_type)
                elif sort_by == "Claim Settlement":
                    self.terminsurance.sort_by_claim_settlement(sort_by_type)

                self.driver.implicitly_wait(10)

                policies = self.terminsurance.get_result_insurance_policies()
                print(len(policies))

                # self.logger.info(f"")
                self.logger.info(" ")
                self.logger.info(f"For Rs {life_coverage_amount}, for {coverage_years} years, and {premium_type} investments".center(75, "_"))
                for i in range(len(policies)):
                    element = policies[i]
                    self.logger.info(f"Name: {element['name']} Life Cover: {element['lifecover'][1:]} Claim Settled: {element['claimsetteled']} Price: {element['name']}")
                    writeData("Term_Life_Insurance_List", indexing, i+6, f"Name: {element['name']} Life Cover: {element['lifecover']} Claim Settled: {element['claimsetteled']} Price: {element['name']}")
            except Exception as e:
                self.logger.info(f"For Rs {life_coverage_amount}, for {coverage_years} years, and {premium_type} investments".center(75, "_"))
                self.logger.info("Failed report:")
                self.logger.error(e)


        assert True
        self.driver.close()



class Test_TermInsurancePlans:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_Plan_Page_Title(self, setup):

        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Plans Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        self.homepage.term_insurance()
        self.driver.implicitly_wait(10)

        self.terminsurance = TermInsurancePage(self.driver)
        self.driver.implicitly_wait(10)
        self.terminsurance.term_insurance_plan()
        self.driver.implicitly_wait(10)

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance - Buy Best Term Insurance Plan and Policy Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceTerminalogies:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_Terminalogies_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Terminalogies Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.term_insurance_terminalogies()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance Terminology - Common Terms used in Term Insurance | Policybazaar":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_WhatIsTermInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_What_Is_Term_Insurance_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of What Is Term Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.what_is_term_insurance()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"What is Term Insurance? | Term Insurance Definition & Benefits":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_NoCostTermInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_No_Cost_Term_Insurance_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of No Cost Term Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.no_cost_term_insurance()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance with 100% Refund of Premium at NO COST":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceForNRI:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_For_NRI_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance For NRI Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.term_insurance_for_nri()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance - Buy Best Term Insurance Plan and Policy Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceForWomen:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_For_Women_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance For Women Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.term_insurance_for_women()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance for Women":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceForHousewife:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_For_Housewife_Page_Title(self, setup):

        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance For Housewife Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.term_insurance_for_housewife()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance Plan For Housewife | Need of Term Plan For Housewife":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_BestTermInsurancePlans:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Best_Term_Insurance_Plans_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Best Term Insurance Plans Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.best_term_insurance_plans()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == "Best Term Insurance Plans in India {}, {}".format(datetime.date.today().strftime("%B"), datetime.date.today().year):
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_LifeInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Life_Insurance_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Life Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.life_insurance()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Life Insurance Policy - Best Life Insurance Plans in India {datetime.date.today().year} | Policybazaar Life Insurance":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_OneCroreTermInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_One_Crore_Term_Insurance_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of 1 Crore Term Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.one_crore_term_insurance()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"1 Crore Term Insurance Plan - Buy ₹1 Crore Term Insurance Premium Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceCalculator:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_Calculator_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Insurance Calculator Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.term_insurance_calculator()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance Plan Calculator Online {datetime.date.today().year} | Policybazaar":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceReturnOfPremium:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Term_Insurance_Return_Of_Premium_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance return of Premium Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.term_insurance_return_of_premium()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Plan with Return of Premium - TROP {datetime.date.today().year} | Policybazaar":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_SaralJeevanBima:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Saral_Jeevan_Bima_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Saraj Jeevan Bima Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.saral_jeevan_bima()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Saral Jeevan Bima Yojana : Coverage, Benefits & Eligibility":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_DedicatedClaimAssistance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check

    def test_Dedicated_Claim_Assistance_Page_Title(self, setup):

        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Dedicated Claim Assistance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)
        self.terminsurance.dedicated_claim_assistance()

        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Pbclaim":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False
