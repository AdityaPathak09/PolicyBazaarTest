import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from threading import Thread

class InvestmentPlansPage:

    popup_ad_id = "exit-intent-popup-container"
    btn_close_popup_ad_id = "exit-intent-popup-close"

    dropdown_Investment_Plans_Xpath = "/html/body/div[1]/nav/div/div[2]/div/div[3]/ul/li[2]/div/a/span"
    list_elements_under_dropdown_Investment_Plans_Xpath = "/html/body/div[1]/nav/div/div[2]/div/div[3]/ul/li[2]/ul/li"
    link_sip_calculator_Xpath = "/html/body/div[1]/nav/div/div[2]/div/div[3]/ul/li[2]/ul/li[4]/a/span"

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)


    def sip_calculator(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Investment_Plans_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_sip_calculator_Xpath).click()
        self.driver.implicitly_wait(10)

    def get_list_elements_under_Investment_Plans(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Investment_Plans_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        elements = self.driver.find_elements(By.XPATH, self.list_elements_under_dropdown_Investment_Plans_Xpath)
        self.driver.implicitly_wait(10)

        return [element.text for element in elements]



class SIPCalculatorPage:

    I_Know_my_investment_amount_Xpath = "//*[@id='topForm']/div[1]/div/div[1]/label[1]"
    I_Know_my_goal_amount_Xpath = "//*[@id='topForm']/div[1]/div/div[1]/label[2]"
    rd_lumpsum_Xpath = "//*[@id='invest-amount']/div/div[1]/div[1]/label[3]"
    rd_Yearly_SIP_Xpath = "//*[@id='invest-amount']/div/div[1]/div[1]/label[2]"
    rd_Monthly_SIP_Xpath = "//*[@id='invest-amount']/div/div[1]/div[1]/label[1]"
    text_Investment_Amount_Xpath = "//*[@id='sipAmtInvest']"
    text_Investment_Year_Xpath = "//*[@id='sipInvTerm']"
    text_Investment_Return_Xpath = "//*[@id='sipExpectedROI']"
    text_Investment_Value_Xpath = "/html/body/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[2]/section[1]/div/div[2]/div[2]/span[2]"
    text_Investment_Amount_Goal_Xpath = "/html/body/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[2]/section[2]/div/div[1]/div/div[1]/div[2]/input"
    text_Investment_Year_Goal_Xpath = "/html/body/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[2]/section[2]/div/div[1]/div/div[2]/div[1]/div[2]/input"
    text_Investment_Return_Goal_Xpath = "/html/body/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[2]/section[2]/div/div[1]/div/div[3]/div[1]/div[2]/input"
    text_Investment_Value_Goal_Xpath = "/html/body/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div[2]/section[2]/div/div[2]/div[2]/span[2]"

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def click_I_Know_my_investment_amount(self):
        self.driver.find_element(By.XPATH, self.I_Know_my_investment_amount_Xpath).click()
        self.driver.implicitly_wait(10)

    def click_I_Know_my_goal_amount(self):
        self.driver.find_element(By.XPATH, self.I_Know_my_goal_amount_Xpath).click()
        self.driver.implicitly_wait(10)

    def click_rd_Monthly_SIP(self):
        self.driver.find_element(By.XPATH, self.rd_Monthly_SIP_Xpath).click()
        self.driver.implicitly_wait(10)

    def click_rd_Yearly_SIP(self):
        self.driver.find_element(By.XPATH, self.rd_Yearly_SIP_Xpath).click()
        self.driver.implicitly_wait(10)

    def click_rd_Lumpsum_SIP(self):
        self.driver.find_element(By.XPATH, self.rd_lumpsum_Xpath).click()
        self.driver.implicitly_wait(10)

    def set_text_Investment_Amount(self, data):
        text_Investment_Amount = self.driver.find_element(By.XPATH, self.text_Investment_Amount_Xpath)
        self.driver.implicitly_wait(10)
        text_Investment_Amount.clear()
        self.driver.implicitly_wait(10)
        text_Investment_Amount.send_keys(data)

    def set_text_Investment_Year(self, data):
        text_Investment_Year = self.driver.find_element(By.XPATH, self.text_Investment_Year_Xpath)
        self.driver.implicitly_wait(10)
        text_Investment_Year.clear()
        self.driver.implicitly_wait(10)
        text_Investment_Year.send_keys(data)

    def set_text_Investment_Return(self, data):
        text_Investment_Return = self.driver.find_element(By.XPATH, self.text_Investment_Return_Xpath)
        self.driver.implicitly_wait(10)
        text_Investment_Return.clear()
        self.driver.implicitly_wait(10)
        text_Investment_Return.send_keys(data)

    def get_Investment_Value(self):
        text_Investment_Value = self.driver.find_element(By.XPATH, self.text_Investment_Value_Xpath)
        self.driver.implicitly_wait(10)
        return text_Investment_Value.text

    def set_text_Investment_Amount_Goal(self, data):
        text_Investment_Amount_Goal = self.driver.find_element(By.XPATH, self.text_Investment_Amount_Goal_Xpath)
        self.driver.implicitly_wait(10)
        text_Investment_Amount_Goal.clear()
        self.driver.implicitly_wait(10)
        text_Investment_Amount_Goal.send_keys(data)

    def set_text_Investment_Year_Goal(self, data):
        text_Investment_Year_Goal = self.driver.find_element(By.XPATH, self.text_Investment_Year_Goal_Xpath)
        self.driver.implicitly_wait(10)
        text_Investment_Year_Goal.clear()
        self.driver.implicitly_wait(10)
        text_Investment_Year_Goal.send_keys(data)

    def set_text_Investment_Return_Goal(self, data):
        text_Investment_Return_Goal = self.driver.find_element(By.XPATH, self.text_Investment_Return_Goal_Xpath)
        self.driver.implicitly_wait(10)
        text_Investment_Return_Goal.clear()
        self.driver.implicitly_wait(10)
        text_Investment_Return_Goal.send_keys(data)

    def get_text_Investment_Value_Goal(self):
        text_Investment_Value_Goal = self.driver.find_element(By.XPATH, self.text_Investment_Value_Goal_Xpath)
        self.driver.implicitly_wait(10)
        return text_Investment_Value_Goal.text



