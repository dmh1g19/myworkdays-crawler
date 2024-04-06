from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from utils import *
import time
import json

class CrawlerMyInfo:
    def __init__(self, driver_path, data):
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.data = data

    def get_website(self, url):
        self.driver.get(url)
    
    def kill_driver(self):
        self.driver.quit()

    def get_driver(self):
        return self.driver

    def sign_in(self):
        try:
            print("Logging in")
            static_input("//input[@data-automation-id='email']", self.data["email"], self.driver)
            static_input("//input[@data-automation-id='password']", self.data["password"], self.driver)

            # Click sign-in button
            # There's a <div> (filter div) capturing clicks acting as the button, the <button> itself is not the target
            click_button("click_filter", self.driver)
            time.sleep(5) 
        except Exception as e:
            print("Error in sign_in")
            print(e)
        finally:
            print("Done...\n")

    def where_did_you_hear_about_us(self):
        try:
            scroll_to_bottom_then_top(self.driver)
            print("Filling \"Where did you hear about us?\"")
            complex_drop_down("//div[@data-automation-id='multiSelectContainer']", "input[data-automation-id='searchBox']", "LinkedIn", "//p[@data-automation-label='LinkedIn']", self.driver)
        except Exception as e:
            print("Error in \"Where did you hear about us?\"")
            #print(e)
        finally:
            print("Done...\n")

    def have_you_worked_for_us_before(self):
        try:
            print("Filling \"have you worked for us before?\"")
            radial_input_no("previousWorker", ".//label[contains(text(), 'No')]", "for", self.driver)
            time.sleep(1) 
        except Exception as e:
            print("Error in \"Have you worked for us before?\"")
            print(e)
        finally:
            print("Done...\n")

    def select_country(self):
        try:
            print("Selecting country from drop down.")
            simple_drop_down(f"//button[@data-automation-id='countryDropdown']", f"//li[@data-value='29247e57dbaf46fb855b224e03170bc7']", self.driver)
            time.sleep(2) 
        except Exception as e:
            print("Error in country drop down select.")
            print(e)
        finally:
            print("Done...\n")

    def select_name_prefix(self):
        try:
            print("Selecting naming prefex.")
            simple_drop_down(f"//button[@data-automation-id='legalNameSection_title']", f"//li[@data-value='8c5fc5940f0b014912758294b400c22f']", self.driver) # Mr: 8c5fc5940f0b014912758294b400c22f
            time.sleep(2) 
        except Exception as e:
            print("Error selecting name prefix.")
            print(e)
        finally:
            print("Done...\n")

    def enter_name_and_surname(self):
        try:
            print("Entering name and surname.")
            static_input("//input[@data-automation-id='legalNameSection_firstName']", self.data["name"], self.driver)
            static_input("//input[@data-automation-id='legalNameSection_lastName']", self.data["surname"], self.driver)
            time.sleep(1) 
        except Exception as e:
            print("Error entering name and surname.")
            print(e)
        finally:
            print("Done...\n") 
 
    def enter_address(self):
        try:
            print("Entering address.")
            static_input("//input[@data-automation-id='addressSection_addressLine1']", self.data["addr"], self.driver)
            static_input("//input[@data-automation-id='addressSection_city']", self.data["city"], self.driver)
            simple_drop_down(f"//button[@data-automation-id='addressSection_countryRegion']", f"//li[@data-value='42a98072ea70411dabde47d538d4f156']", self.driver) # HAMPSHIRE = 42a98072ea70411dabde47d538d4f156
            static_input("//input[@data-automation-id='addressSection_postalCode']", self.data["postcode"], self.driver)
        except Exception as e:
            print("Error entering address.")
            print(e)
        finally:
            print("Done...\n") 

    def enter_phone(self):
        try:
            print("Entering phone.")
            simple_drop_down(f"//button[@data-automation-id='phone-device-type']", f"//li[@data-value='8c5fc5940f0b01db13a71f59af004207']", self.driver) # MOBILE = 8c5fc5940f0b01db13a71f59af004207
            time.sleep(3)

            container = "//div[@data-automation-id='multiSelectContainer'][@data-automation-id-prompt='country-phone-code']"
            input_box = "input[data-automation-id='searchBox']"
            search_query = "united kingdom"
            item_element_id = "//p[@data-automation-label='United Kingdom (+44)']"
            complex_drop_down(container, input_box, search_query, item_element_id, self.driver)
            time.sleep(2)

            #static_input("phone-number", self.data["phone"], self.driver)
            static_input("//input[@data-automation-id='phone-number']", self.data["phone"], self.driver)
        except Exception as e:
            #Sometimes the form auto populates this field so it might fail, in which case continue as normal
            print("Error entering phone.")
            print("Is the field already populated?")
            static_input("//input[@data-automation-id='phone-number']", self.data["phone"], self.driver)
        finally:
            pass

    def press_submit_button(self):
        try:
            print("Pressing button.")
            click_button2("//button[@data-automation-id='bottom-navigation-next-button']", self.driver)
        except Exception as e:
            print("Error pressing button.")
            print(e)
        finally:
            print("Done...\n") 

