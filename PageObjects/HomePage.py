import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    dropdown_Insurance_Products_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[2]/a[1]"
    dropdown_Renew_Your_Policy_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[3]/a[1]"
    dropdown_Claim_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[4]/a[1]"
    dropdown_Support_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[5]/a[1]"
    button_Sign_In_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[7]/a[1]"

    link_Term_Insurance_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/h3[1]/a[1]"
    link_Investment_Plans_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[2]/h3[1]/a[1]"
    link_Health_Insurance_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[3]/h3[1]/a[1]"
    link_Car_Insurance_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[4]/h3[1]/a[1]"
    link_Other_Insurance_Xpath = "/html[1]/body[1]/div[5]/div[2]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/h3[2]/a[1]"


    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def term_insurance(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.dropdown_Insurance_Products_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.link_Term_Insurance_Xpath)).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def investment_plans(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.dropdown_Insurance_Products_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.link_Investment_Plans_Xpath)).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def health_insurance(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.dropdown_Insurance_Products_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.link_Health_Insurance_Xpath)).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def car_insurance(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.dropdown_Insurance_Products_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.link_Car_Insurance_Xpath)).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def other_insurance(self):
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.dropdown_Insurance_Products_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        self.action.move_to_element(self.driver.find_element(By.XPATH,  self.link_Other_Insurance_Xpath)).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)
