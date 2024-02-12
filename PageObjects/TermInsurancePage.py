import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from threading import Thread


class TermInsurancePage:

    # Identifiers for popup
    popup_ad_id = "exit-intent-popup-container"
    btn_close_popup_ad_id = "exit-intent-popup-close"

    # Dropdown and link XPaths
    dropdown_Term_Insurance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/div/a/span"
    list_elements_under_dropdown_Term_Insurance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li"

    link_Term_Insurance_Plan_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[1]/a/span"
    link_Term_Insurance_Terminology_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[2]/a/span"
    link_What_Is_Term_Insurance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[3]/a/span"
    link_No_Cost_Term_Insurance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[4]/a/span"
    link_Term_Insurance_For_NRI_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[5]/a/span"
    link_Term_Insurance_For_Women_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[6]/a/span"
    link_Term_Insurance_For_Housewife_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[7]/a/span"
    link_Best_Term_Insurance_Plans_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[8]/a/span"
    link_Life_Insurance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[9]/a/span"
    link_1_Crore_Term_Insurance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[10]/a/span"
    link_Term_Insurance_Calculator_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[11]/a/span"
    link_Term_Insurance_Return_Of_Premium_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[12]/a/span"
    link_Saral_Jeevan_Bima_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[13]/a/span"
    link_Dedicated_Claim_Assistance_Xpath = "/html/body/div[2]/nav/div/div[2]/div/div[3]/ul/li[1]/ul/li[14]/a/span"

    # Dropdowns and buttons for insurance calculator
    dropdown_Life_Cover_Amount_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[2]/div/div[1]"
    dropdown_Coverage_Till_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[3]/div/div[1]"
    btn_Monthly_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[5]/div[1]/button[1]"
    btn_Yearly_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[5]/div[1]/button[2]"
    dropdown_Sorting_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[6]/div[1]"
    dropdown_All_Insurers_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[7]/div[1]"

    btn_Sort_By_Price_Low_To_High_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]"
    btn_Sort_By_Price_High_To_Low_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[6]/div[2]/div[2]/div[2]"

    btn_Sort_By_Claim_Settlelment_Low_To_High_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[6]/div[2]/div[4]/div[1]"
    btn_Clear_Filter_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[6]/div[2]/div[4]/div[1]"

    btn_Sort_By_Claim_Settlelment_High_To_Low_Xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[6]/div[2]/div[4]/div[2]"

    def close_popup(self, driver):
        # Method to close popups using a separate thread
        action = ActionChains(driver)

        while True:

            try:
                popup_close_2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[32]/span")
                popup_close_1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[33]/div/div[1]")

                if popup_close_1.is_displayed():
                    # Attempt to find and close the first type of popup

                    action.move_to_element(popup_close_1).pause(0.2).click().perform()
                    # popup_close_1.click()
                    driver.implicitly_wait(10)

                if popup_close_2.is_displayed():
                     # Attempt to find and close the second type of popup

                    # action.move_to_element(popup_close_2).pause(0.2).click().perform()
                    popup_close_2.click()
                    driver.implicitly_wait(10)

            except:
                pass

            time.sleep(0.05)

    def __init__(self, driver):
        # Initialize the TermInsurancePage with the driver and start the popup handling thread

        self.driver = driver
        self.action = ActionChains(driver)

        close_popup_thread = Thread(target=self.close_popup, args=(self.driver,))
        close_popup_thread.daemon = True
        close_popup_thread.start()

    def term_insurance_plan(self):
        # Method to navigate to the term insurance plan page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_Plan_Xpath).click()
        self.driver.implicitly_wait(10)

    def term_insurance_terminalogies(self):
        # Method to navigate to the term insurance terminologies page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_Terminology_Xpath).click()
        self.driver.implicitly_wait(10)

    def what_is_term_insurance(self):
        # Method to navigate to the What is term insurance page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_What_Is_Term_Insurance_Xpath).click()
        self.driver.implicitly_wait(10)

    def no_cost_term_insurance(self):
        # Method to navigate to the no cost term insurance page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_No_Cost_Term_Insurance_Xpath).click()
        self.driver.implicitly_wait(10)

    def term_insurance_for_nri(self):
        # Method to navigate to the term insurance for NRI page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_Plan_Xpath).click()
        self.driver.implicitly_wait(10)

    def term_insurance_for_women(self):
        # Method to navigate to the term insurance for women page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_For_Women_Xpath).click()
        self.driver.implicitly_wait(10)

    def term_insurance_for_housewife(self):
        # Method to navigate to the term insurance for housewife page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_For_Housewife_Xpath).click()
        self.driver.implicitly_wait(10)

    def best_term_insurance_plans(self):
        # Method to navigate to the best term insurance plans page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Best_Term_Insurance_Plans_Xpath).click()
        self.driver.implicitly_wait(10)

    def life_insurance(self):
        # Method to navigate to the life insurance page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Life_Insurance_Xpath).click()
        self.driver.implicitly_wait(10)

    def one_crore_term_insurance(self):
        # Method to navigate to the one crore term insurance plan page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_1_Crore_Term_Insurance_Xpath).click()
        self.driver.implicitly_wait(10)

    def term_insurance_calculator(self):
        # Method to navigate to the term insurance calculator page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_Calculator_Xpath).click()
        self.driver.implicitly_wait(10)

    def term_insurance_return_of_premium(self):
        # Method to navigate to the term insurance return of premium page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Term_Insurance_Return_Of_Premium_Xpath).click()
        self.driver.implicitly_wait(10)

    def saral_jeevan_bima(self):
        # Method to navigate to the saral jeevan bima page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Saral_Jeevan_Bima_Xpath).click()
        self.driver.implicitly_wait(10)

    def dedicated_claim_assistance(self):
        # Method to navigate to the dedicated claim assistance page

        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(
            0.2).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_Dedicated_Claim_Assistance_Xpath).click()
        self.driver.implicitly_wait(10)

    def select_life_cover_amount(self, amount):
        # Locate the dropdown for life cover amount
        dropdown_life_cover_amt = self.driver.find_element(By.XPATH, self.dropdown_Life_Cover_Amount_Xpath)

        try:
            # Attempt to click on the dropdown directly
            dropdown_life_cover_amt.click()
            self.driver.implicitly_wait(10)
        except:
            try:
                # If clicking directly fails, try scrolling down and then clicking
                self.action.scroll_by_amount(0, 100).perform()
                self.driver.implicitly_wait(10)
                dropdown_life_cover_amt.click()
                self.driver.implicitly_wait(10)
            except:
                # If scrolling down also fails, scroll up and then click
                self.action.scroll_by_amount(0, -200).perform()
                self.driver.implicitly_wait(10)
                dropdown_life_cover_amt.click()
                self.driver.implicitly_wait(10)

        # XPath for different life cover amount options
        list_1_crore_xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[2]"
        list_1_25_crore_xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[3]"
        list_1_5_crore_xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[4]"
        list_1_75_crore_xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[5]"
        list_2_crore_xpath = "/html/body/div[3]/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[6]"

        # Map the desired amount to the corresponding XPath and click
        if amount == 1:
            option = self.driver.find_element(By.XPATH, list_1_crore_xpath)
        elif amount == 1.25:
            option = self.driver.find_element(By.XPATH, list_1_25_crore_xpath)
        elif amount == 1.5:
            option = self.driver.find_element(By.XPATH, list_1_5_crore_xpath)
        elif amount == 1.75:
            option = self.driver.find_element(By.XPATH, list_1_75_crore_xpath)
        elif amount == 2:
            option = self.driver.find_element(By.XPATH, list_2_crore_xpath)
        else:
            # Default to 1 crore if amount is not in the specified options
            option = self.driver.find_element(By.XPATH, list_1_crore_xpath)

        # Perform the click after moving to the selected option
        self.driver.implicitly_wait(10)
        self.action.move_to_element(option).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def select_coverage_till(self, years):
        # Locate the Coverage Till dropdown
        dropdown_Coverage_Till = self.driver.find_element(By.XPATH, self.dropdown_Coverage_Till_Xpath)

        self.driver.implicitly_wait(10)
        dropdown_Coverage_Till.click()
        self.driver.implicitly_wait(10)

        # If years is greater than 22, select the corresponding option based on the index
        if years > 22:
            index = years - 22 + 1
            option = self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[1]/div[3]/div/div[2]/div[{index}]")
            self.driver.implicitly_wait(10)
            self.action.move_to_element(option).pause(0.2).click().perform()
            self.driver.implicitly_wait(10)

    def press_Monthly_button(self):
        # Locate and click on the Monthly button
        btn = self.driver.find_element(By.XPATH, self.btn_Monthly_Xpath)
        self.driver.implicitly_wait(10)
        self.action.move_to_element(btn).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def press_Yearly_button(self):
        # Locate and click on the Yearly button
        btn = self.driver.find_element(By.XPATH, self.btn_Yearly_Xpath)
        self.driver.implicitly_wait(10)
        self.action.move_to_element(btn).pause(0.2).click().perform()
        self.driver.implicitly_wait(10)

    def sort_by_price(self, condition):
        # Locate the Sorting dropdown and click on it
        dropdown_sort = self.driver.find_element(By.XPATH, self.dropdown_Sorting_Xpath)
        self.driver.implicitly_wait(10)
        self.action.move_to_element(dropdown_sort).pause(0.2).click().perform()

        # Choose sorting condition based on input
        if condition == "Low to High":
            btn = self.driver.find_element(By.XPATH, self.btn_Sort_By_Price_Low_To_High_Xpath)
            self.driver.implicitly_wait(10)
            self.action.move_to_element(btn).pause(0.2).click().perform()
        elif condition == "High to Low":
            btn = self.driver.find_element(By.XPATH, self.btn_Sort_By_Price_High_To_Low_Xpath)
            self.driver.implicitly_wait(10)
            self.action.move_to_element(btn).pause(0.2).click().perform()

    def sort_by_claim_settlement(self, condition):
        # Locate the Sorting dropdown and click on it
        dropdown_sort = self.driver.find_element(By.XPATH, self.dropdown_Sorting_Xpath)
        self.driver.implicitly_wait(10)
        self.action.move_to_element(dropdown_sort).pause(0.2).click().perform()

        # Choose sorting condition based on input
        if condition == "Low to High":
            btn = self.driver.find_element(By.XPATH, self.btn_Sort_By_Claim_Settlelment_Low_To_High_Xpath)
            self.driver.implicitly_wait(10)
            self.action.move_to_element(btn).pause(0.2).click().perform()
        elif condition == "High to Low":
            btn = self.driver.find_element(By.XPATH, self.btn_Sort_By_Claim_Settlelment_Low_To_High_Xpath)
            self.driver.implicitly_wait(10)
            self.action.move_to_element(btn).pause(0.2).click().perform()

    def get_result_insurance_policies(self):
        try:
            list_xpath = "/html/body/div[3]/div[5]/div[2]/div[2]/div/div"
            term_insurance_policies = self.driver.find_elements(By.XPATH, list_xpath)
            self.driver.implicitly_wait(10)

            policies = []

            print(f"____________length of all elements found: {len(term_insurance_policies)}___________")

            # Check if there is a "View More" button and click it to load more policies
            if self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{len(term_insurance_policies)}]").text == "View More":
                self.action.move_to_element(self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{len(term_insurance_policies)}]")).pause(0.2).scroll_by_amount(0, 100).pause(0.2).perform()
                self.action.move_to_element(self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{len(term_insurance_policies)}]")).pause(0.2).click().perform()
                self.driver.implicitly_wait(10)

            for i in range(len(term_insurance_policies)):
                try:
                    policy_info = dict()
                    try:
                        # Scroll to the current policy element
                        self.action.move_to_element(self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{i+1}]")).pause(0.3).perform()
                        self.driver.implicitly_wait(10)
                    except:
                        pass

                    # Extract information for each policy
                    policy_info["name"] = self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{i+1}]/div/div[1]/div[2]/span").text
                    policy_info["lifecover"] = self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{i+1}]/div/div[2]/p[2]").text
                    policy_info["claimsetteled"] = self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{i+1}]/div/div[3]/p[2]").text
                    policy_info["price"] = self.driver.find_element(By.XPATH, f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{i+1}]/div/div[4]/p[2]").text
                    policy_info["viewbutton"] = f"/html/body/div[3]/div[5]/div[2]/div[2]/div/div[{i+1}]/div/div[5]/button"

                    self.driver.implicitly_wait(10)
                    policies.append(policy_info)
                except:
                    pass
            return policies
        except:
            return []

    def get_list_elements_under_Temrm_Insurence(self):
        # Move to the Term Insurance dropdown and get the list of elements under it
        self.action.move_to_element(self.driver.find_element(By.XPATH, self.dropdown_Term_Insurance_Xpath)).pause(0.2).perform()
        self.driver.implicitly_wait(10)
        elements = self.driver.find_elements(By.XPATH, self.list_elements_under_dropdown_Term_Insurance_Xpath)
        self.driver.implicitly_wait(10)

        return [element.text for element in elements]




class TermInsuranceTerminologies:

    def __init__(self, driver):
        # Initialize the class with the provided WebDriver instance
        self.driver = driver
        self.action = ActionChains(driver)

    # XPaths for various elements
    headings_Term_Insurance_Terminologies_Xpath = "/html/body/div[3]/section/div[3]/div/section/div[1]/div[2]/div/div"
    list_Term_Insurance_Terminologies_names_Xpath = "/html/body/div[3]/section/div[3]/div/section/div[1]/div[2]/div/div"
    list_Term_Insurance_Terminologies_description_Xpath = "/html/body/div[3]/section/div[3]/div/section/div[1]/div[2]/div/div[{}]/div[{}]/div/p/text()"

    # Not Working
    def get_list_of_terminalogies(self, logger):
        # Find all section elements
        section_elements = self.driver.find_elements(By.XPATH, self.headings_Term_Insurance_Terminologies_Xpath)
        self.driver.implicitly_wait(10)

        all_terminalogies = {}

        print(len(section_elements))

        # Iterate through each section
        for index in range(1, len(section_elements) + 1):

            # Get the number of terminologies in the current section
            num_of_terminologies = len(self.driver.find_elements(By.XPATH, self.headings_Term_Insurance_Terminologies_Xpath + f"[{index}]/div"))
            print(num_of_terminologies)

            # Iterate through each terminology in the current section
            for i in range(1, num_of_terminologies + 1):
                # Find names of terminologies
                names = self.driver.find_elements(By.XPATH, self.headings_Term_Insurance_Terminologies_Xpath + f"[{index}]/div[{i}]/div/p/span")
                self.driver.implicitly_wait(10)
                print(" __ ")

                # Print and store names
                for desc in names:
                    print(desc.text)

                # Find descriptions of terminologies
                description = self.driver.find_elements(By.XPATH, self.headings_Term_Insurance_Terminologies_Xpath + f"[{index}]/div[{i}]/div/p")
                self.driver.implicitly_wait(10)

                # Print and store descriptions
                for desc in description:
                    print(desc.text)

                # Store names and descriptions in the dictionary
                for index in range(len(names)):
                    all_terminalogies[names[index]] = description[index]

        return all_terminalogies


