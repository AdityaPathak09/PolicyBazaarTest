import datetime
import inspect
import time

import pytest

from PageObjects.HomePage import HomePage
from PageObjects.TermInsurancePage import TermInsurancePage, TermInsuranceTerminologies
from Utilities.ReadProperties import ReadConfig
from Utilities.logger import LogGen
from Utilities.XLUtils import *

class Test_TermInsurance:

    Application_URL = ReadConfig.getApplicationURL()

    # this function verifies page title of web page
    @pytest.mark.title_check
    @pytest.mark.term_insurance
    def test_Term_Insurance_Page_Title(self, setup):

        # create driver and logger instance
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Page".center(75, "_"))

        # launch policy bazaar
        self.driver.get(self.Application_URL)
        self.driver.implicitly_wait(10)

        # creating home page instance
        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        # print(f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}")
        # print(f"Page Title: {self.driver.title}")

        # checking title of homepage
        if self.driver.title == f"Term Insurance - Buy Best Term Insurance Plan and Policy Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True

        # if title is not as expected, save screenshot
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

    # get list of all links under heading
    @pytest.mark.list_of_term_insurances
    @pytest.mark.term_insurance
    def test_get_list_of_elements_under_Term_Insurance_dropdown(self, setup):

        # create driver and logger instance
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Printing all elements under Term Insurance section".center(100, "_"))

        # launch policy bazaar
        self.driver.get(self.Application_URL)
        self.driver.implicitly_wait(10)

        # creating home page instance
        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        # creating term insurance page object
        self.terminsurance = TermInsurancePage(self.driver)
        list_of_elements = self.terminsurance.get_list_elements_under_Temrm_Insurence()

        # printing names
        for element in list_of_elements:
            print(element)
            self.logger.info(element)

        # closing driver
        self.driver.close()
        assert True


    # this function gets list of term insurances acording to given parameters
    @pytest.mark.term_insurance
    @pytest.mark.term_insurance_plans
    def test_term_insurance_plans_list(self, setup):

        # create driver and logger instance
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Term Insurance List")

        # launch policy bazaar
        self.driver.get(self.Application_URL)
        self.driver.implicitly_wait(10)

        # creating home page instance
        self.homepage = HomePage(self.driver)
        self.homepage.term_insurance()

        # creating term insurance page instance
        self.terminsurance = TermInsurancePage(self.driver)

        # iterating through excel data
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

                # saving policies to excel
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
    @pytest.mark.term_insurance_plans
    def test_Term_Insurance_Plan_Page_Title(self, setup):
        """
        Test the Title of Term Insurance Plans Page.

        This method initializes the test environment, navigates to the Term Insurance Plans page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Plans Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.driver.implicitly_wait(10)

        # Navigate to the Term Insurance Plans page
        self.homepage.term_insurance()
        self.driver.implicitly_wait(10)

        self.terminsurance = TermInsurancePage(self.driver)
        self.driver.implicitly_wait(10)

        # Click on the Term Insurance Plans link
        self.terminsurance.term_insurance_plan()
        self.driver.implicitly_wait(10)

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance - Buy Best Term Insurance Plan and Policy Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceTerminalogies:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.term_insurance_terminologies
    def test_Term_Insurance_Terminalogies_Page_Title(self, setup):
        """
        Test the Title of Term Insurance Terminologies Page.

        This method initializes the test environment, navigates to the Term Insurance Terminologies page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Terminologies Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Term Insurance Terminologies page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Term Insurance Terminologies link
        self.terminsurance.term_insurance_terminalogies()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance Terminology - Common Terms used in Term Insurance | Policybazaar":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


    # @pytest.mark.getList
    # def test_Term_Insurance_Terminalogies_List(self, setup):
    #
    #     self.driver = setup
    #
    #     self.logger = LogGen.loggen()
    #     self.logger.info("getting Title of Term Insurance Terminologies List".center(75, "_"))
    #
    #     self.driver.get(self.ApplicationURL)
    #     self.driver.implicitly_wait(10)
    #
    #     self.homepage = HomePage(self.driver)
    #     self.homepage.term_insurance()
    #
    #     self.terminsurance = TermInsurancePage(self.driver)
    #     self.terminsurance.term_insurance_terminalogies()
    #
    #     self.terminsuranceterminologies = TermInsuranceTerminologies(self.driver)
    #
    #     all_terminologies = self.terminsuranceterminologies.get_list_of_terminalogies(self.logger)

class Test_WhatIsTermInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.what_is_term_insurance
    def test_What_Is_Term_Insurance_Page_Title(self, setup):
        """
        Test the Title of What Is Term Insurance Page.

        This method initializes the test environment, navigates to the What Is Term Insurance page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of What Is Term Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the What Is Term Insurance page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the What Is Term Insurance link
        self.terminsurance.what_is_term_insurance()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"What is Term Insurance? | Term Insurance Definition & Benefits":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_NoCostTermInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.no_cost_term_insurance
    def test_No_Cost_Term_Insurance_Page_Title(self, setup):
        """
        Test the Title of No Cost Term Insurance Page.

        This method initializes the test environment, navigates to the No Cost Term Insurance page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of No Cost Term Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the No Cost Term Insurance page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the No Cost Term Insurance link
        self.terminsurance.no_cost_term_insurance()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance with 100% Refund of Premium at NO COST":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False

class Test_TermInsuranceForNRI:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.term_insurance_for_nri
    def test_Term_Insurance_For_NRI_Page_Title(self, setup):
        """
        Test the Title of Term Insurance For NRI Page.

        This method initializes the test environment, navigates to the Term Insurance For NRI page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance For NRI Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Term Insurance For NRI page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Term Insurance For NRI link
        self.terminsurance.term_insurance_for_nri()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance - Buy Best Term Insurance Plan and Policy Online in {datetime.date.today().year}":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_TermInsuranceForWomen:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.term_insurance_for_women
    def test_Term_Insurance_For_Women_Page_Title(self, setup):
        """
        Test the Title of Term Insurance For Women Page.

        This method initializes the test environment, navigates to the Term Insurance For Women page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance For Women Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Term Insurance For Women page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Term Insurance For Women link
        self.terminsurance.term_insurance_for_women()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance for Women":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_TermInsuranceForHousewife:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.term_insurance_for_housewife
    def test_Term_Insurance_For_Housewife_Page_Title(self, setup):
        """
        Test the Title of Term Insurance For Housewife Page.

        This method initializes the test environment, navigates to the Term Insurance For Housewife page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance For Housewife Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Term Insurance For Housewife page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Term Insurance For Housewife link
        self.terminsurance.term_insurance_for_housewife()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Term Insurance Plan For Housewife | Need of Term Plan For Housewife":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False



class Test_BestTermInsurancePlans:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.best_term_insurance_plans
    def test_Best_Term_Insurance_Plans_Page_Title(self, setup):
        """
        Test the Title of Best Term Insurance Plans Page.

        This method initializes the test environment, navigates to the Best Term Insurance Plans page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Best Term Insurance Plans Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Best Term Insurance Plans page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Best Term Insurance Plans link
        self.terminsurance.best_term_insurance_plans()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = "Best Term Insurance Plans in India {}, {}".format(datetime.date.today().strftime("%B"), datetime.date.today().year)
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_LifeInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.life_insurance
    def test_Life_Insurance_Page_Title(self, setup):
        """
        Test the Title of Life Insurance Page.

        This method initializes the test environment, navigates to the Life Insurance page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Life Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Life Insurance page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Life Insurance link
        self.terminsurance.life_insurance()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = f"Life Insurance Policy - Best Life Insurance Plans in India {datetime.date.today().year} | Policybazaar Life Insurance"
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_OneCroreTermInsurance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.one_crore_term_insurance
    def test_One_Crore_Term_Insurance_Page_Title(self, setup):
        """
        Test the Title of 1 Crore Term Insurance Page.

        This method initializes the test environment, navigates to the 1 Crore Term Insurance page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of 1 Crore Term Insurance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the 1 Crore Term Insurance page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the 1 Crore Term Insurance link
        self.terminsurance.one_crore_term_insurance()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = f"1 Crore Term Insurance Plan - Buy ₹1 Crore Term Insurance Premium Online in {datetime.date.today().year}"
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title.replace('₹', 'Rs')}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_TermInsuranceCalculator:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.term_insurance_calculator
    def test_Term_Insurance_Calculator_Page_Title(self, setup):
        """
        Test the Title of Term Insurance Calculator Page.

        This method initializes the test environment, navigates to the Term Insurance Calculator page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Insurance Calculator Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Term Insurance Calculator page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Term Insurance Calculator link
        self.terminsurance.term_insurance_calculator()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = f"Term Insurance Plan Calculator Online {datetime.date.today().year} | Policybazaar"
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_TermInsuranceReturnOfPremium:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.term_insurance_return_of_premium
    def test_Term_Insurance_Return_Of_Premium_Page_Title(self, setup):
        """
        Test the Title of Term Insurance Return of Premium Page.

        This method initializes the test environment, navigates to the Term Insurance Return of Premium page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Term Insurance Return of Premium Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Term Insurance Return of Premium page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Term Insurance Return of Premium link
        self.terminsurance.term_insurance_return_of_premium()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = f"Term Plan with Return of Premium - TROP {datetime.date.today().year} | Policybazaar"
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_SaralJeevanBima:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.saral_jeevan_beema_yojna
    def test_Saral_Jeevan_Bima_Page_Title(self, setup):
        """
        Test the Title of Saral Jeevan Bima Page.

        This method initializes the test environment, navigates to the Saral Jeevan Bima page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Saraj Jeevan Bima Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Saral Jeevan Bima page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Saral Jeevan Bima link
        self.terminsurance.saral_jeevan_bima()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = f"Saral Jeevan Bima Yojana : Coverage, Benefits & Eligibility"
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False


class Test_DedicatedClaimAssistance:

    ApplicationURL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.dedicated_claim_assistance
    def test_Dedicated_Claim_Assistance_Page_Title(self, setup):
        """
        Test the Title of Dedicated Claim Assistance Page.

        This method initializes the test environment, navigates to the Dedicated Claim Assistance page,
        and verifies if the page title matches the expected format.

        Args:
            setup: The test setup fixture.

        Returns:
            None
        """
        self.driver = setup
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Dedicated Claim Assistance Page".center(75, "_"))

        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)

        # Navigate to the Dedicated Claim Assistance page
        self.homepage.term_insurance()

        self.terminsurance = TermInsurancePage(self.driver)

        # Click on the Dedicated Claim Assistance link
        self.terminsurance.dedicated_claim_assistance()

        # Print and check the page title
        print(f"Page Title: {self.driver.title}")
        expected_title = f"Pbclaim"
        if self.driver.title == expected_title:
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:
            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")

            # Save screenshot on failure
            self.driver.save_screenshot(".\\Screenshots\\TermInsurance\\" + f"{inspect.currentframe().f_code.co_name}{str(datetime.datetime.now().strftime('%d-%m-%Y_%H_%M_%S'))}.png")
            self.driver.close()
            assert False
