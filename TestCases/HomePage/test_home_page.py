import inspect
from datetime import datetime

import pytest

from PageObjects.HomePage import HomePage
from Utilities.ReadProperties import ReadConfig
from Utilities.logger import LogGen

class Test_HomePage:

    Application_URL = ReadConfig.getApplicationURL()

    @pytest.mark.title_check
    @pytest.mark.home_page
    def test_Home_Page_Title(self, setup):
        self.driver = setup
        self.driver.get(self.Application_URL)

        self.logger = LogGen.loggen()
        self.logger.info("Checking Title of Home Page".center(75, "_"))

        print(f"Page Title: {self.driver.title}")

        if self.driver.title == "Insurance - Compare & Buy Insurance Plans – Health, Term, Life, Car":
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



