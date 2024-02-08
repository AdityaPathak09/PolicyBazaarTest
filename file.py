# from Utilities.logger import LogGen
#
# logger = LogGen.loggen()
# logger.info("Hello")

import datetime
import time
import pytest
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
from PageObjects.TermInsurancePage import TermInsurancePage
from PageObjects.InvestmentPlansPage import InvestmentPlansPage
from Utilities.ReadProperties import ReadConfig
from Utilities.XLUtils import *
from Utilities.logger import LogGen


class Test_InvestmentPlans:


    Application_URL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    def test_Investment_Plans_Page_Title(self, setup):

        self.driver = setup
        self.driver.get(self.Application_URL)
        self.driver.implicitly_wait(10)

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Investment Plans Page".center(50, "_"))

        self.homepage = HomePage(self.driver)
        self.homepage.investment_plans()
        print(f"Page Title: {self.driver.title}")
        if self.driver.title == f"Best Investment Plans in India To Invest in {datetime.date.today().year} For High Returns":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:

            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\InvestmentPlans\\" + "Investment_Plans_page_title.png")
            self.driver.close()
            assert False

class Test_SIPCalculator:
    ApplicationURL = ReadConfig.getApplicationURL()
    @pytest.mark.title_check
    @pytest.mark.SIP
    def test_SIP_Calculator_Page_Title(self, setup):
        #Launching Browser
        self.driver = setup
        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)

        #add logger object
        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of SIP Calculator Page".center(50, "_"))

        #Clicking On Investment Plans Link
        self.homepage = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        self.homepage.investment_plans()
        self.driver.implicitly_wait(10)
        #Clicking On Sip Calculator
        self.investmentplans = InvestmentPlansPage(self.driver)
        self.driver.implicitly_wait(10)
        self.investmentplans.sip_calculator()
        self.driver.implicitly_wait(10)
        # Checking Title of the SIP Calculator Page
        if self.driver.title == f"SIP Calculator {datetime.date.today().year} - Check Systematic Investment Plan Returns Online":
            self.logger.info("Case Passed")
            self.logger.info(f"Expected = Actual: {self.driver.title}")
            self.driver.close()
            assert True
        else:

            self.logger.info("Case Failed")
            self.logger.info(f"Expected != Actual: {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\InvestmentPlans\\" + "Term_Insurance_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.SIP
    @pytest.mark.Positive_SIP
    def test_sip_calculator(self, setup):
        #Executing Sip Calculator using Excel Data
        #Launching Browser
        self.driver = setup
        self.driver.get(self.ApplicationURL)
        self.driver.implicitly_wait(10)
        #add logger object
        self.logger = LogGen.loggen()
        self.logger.info("Checking SIP Calculator".center(50, "_"))
        #Click On Investment Plans Page
        self.homepage = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        self.homepage.investment_plans()
        self.driver.implicitly_wait(10)
        #Click On Sip Calculator Page
        self.investmentplans = InvestmentPlansPage(self.driver)
        self.driver.implicitly_wait(10)
        self.investmentplans.sip_calculator()
        self.driver.implicitly_wait(10)
        #Getting Total no of Records in Excel File
        n = getRowCount("Sheet1")
        #Looping for Each Row element execution
        for i in range(2, n+1):
            try:
                #Getting Type Of Investment Calculator Input
                type_of_investment_calculator = readData("Sheet1", i, 1)
                #Selecting The Type Of Investment Calculator
                if type_of_investment_calculator.lower() == "I Know my investment amount".lower():
                    self.investmentplans.click_I_Know_my_investment_amount()
                    # Selecting The Type of Investment with Getting Input from Excel File
                    type_of_investment = readData("Sheet1", i, 2)
                    if type_of_investment.lower() == "Monthly SIP".lower():
                        self.investmentplans.click_rd_Monthly_SIP()
                    elif type_of_investment.lower() == "Yearly SIP".lower():
                        self.investmentplans.click_rd_Yearly_SIP()
                    elif type_of_investment.lower() == "Lumpsum".lower():
                        self.investmentplans.click_rd_Lumpsum_SIP()
                    else:
                        self.driver.save_screenshot(".\\Screenshots\\InvestmentPlans\\" + "SipCalculator.png")
                    #Getting and Entering Investment Amount from Excel File
                    self.investmentplans.set_text_Investment_Amount(readData("Sheet1", i, 3))
                    #Getting and Entering Investment Tenure/Year from Excel File
                    self.investmentplans.set_text_Investment_Year(readData("Sheet1", i, 4))
                    #Getting and Entering Investment Roi from Excel File
                    self.investmentplans.set_text_Investment_Return(readData("Sheet1", i, 5))
                    #Getting Data from Webpage and Entering in Excel File
                    writeData("Sheet1", i, 6, self.investmentplans.get_Investment_Value())
                    self.logger.info(f"For {type_of_investment_calculator}, {type_of_investment}, {readData('Sheet1', i, 3)}, {readData('Sheet1', i, 4)}, {readData('Sheet1', i, 5)}, result is {self.investmentplans.get_Investment_Value()}")
                else:
                    #Selecting The Type Of Investment Calculator
                    self.investmentplans.click_I_Know_my_goal_amount()
                    #Getting and Entering Investment Amount from Excel File
                    self.investmentplans.set_text_Investment_Amount_Goal(readData("Sheet1", i, 3))
                    #Getting and Entering Investment Tenure/Year from Excel File
                    self.investmentplans.set_text_Investment_Year_Goal(readData("Sheet1", i, 4))
                    #Getting and Entering Investment Roi from Excel File
                    self.investmentplans.set_text_Investment_Return_Goal(readData("Sheet1", i, 5))
                    #Getting Data from Webpage and Entering in Excel File
                    writeData("Sheet1", i, 6, self.investmentplans.get_text_Investment_Value_Goal())
                    self.logger.info(f"For \\'I Know my goal amount\\', {type_of_investment}, {readData('Sheet1', i, 3)}, {readData('Sheet1', i, 4)}, {readData('Sheet1', i, 5)}, result is {self.investmentplans.get_text_Investment_Value_Goal()}")
            except:
                #Taking Error Screenshot
                self.driver.save_screenshot(".\\Screenshots\\InvestmentPlans\\" + "SipCalculator.png")
            time.sleep(3)
        self.driver.close()
        self.logger.info("Case Passed")

        assert True
