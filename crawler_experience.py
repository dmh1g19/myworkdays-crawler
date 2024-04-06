from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from utils import *
import time
import json

class CrawlerMyExperience:
    def __init__(self, driver, cv_file_path, data_work_experience, data_education, data_lang):
        self.driver = driver # Driver should already be instantiated from previous page
        self.cv_file_path = cv_file_path
        self.data_work_experience = data_work_experience
        self.data_education = data_education
        self.data_lang = data_lang

    def kill_driver(self):
        self.driver.quit()

    def fill_experience_slots(self):
        try:
            time.sleep(3)
            print("Adding experience, total entries %r." % len(self.data_work_experience))
            click_button2("//button[@aria-label='Add Work Experience' and @data-automation-id='Add']", self.driver)
            time.sleep(3)
            
            for i in range(len(self.data_work_experience)):
                experience = self.data_work_experience[i+1]
                work_experience_xpath = "//div[@data-automation-id='workExperience-%d']" % (i + 1)
                static_input(f"{work_experience_xpath}//input[@data-automation-id='jobTitle']", experience['job_title'], self.driver)
                static_input(f"{work_experience_xpath}//input[@data-automation-id='company']", experience['company'], self.driver)
                static_input(f"{work_experience_xpath}//input[@data-automation-id='location']", experience['location'], self.driver)
            
                fill_date_widget(
                    f"{work_experience_xpath}//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionMonth-display']",
                    f"{work_experience_xpath}//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionYear-display']",
                    experience['from_month'], experience['from_year'], self.driver)
            
                fill_date_widget(
                    f"{work_experience_xpath}//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionMonth-display']",
                    f"{work_experience_xpath}//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionYear-display']",
                    experience['to_month'], experience['to_year'], self.driver)
            
                static_input(f"{work_experience_xpath}//textarea[@data-automation-id='description']", experience['description'], self.driver)
                time.sleep(1)

                if i < len(self.data_work_experience) - 1:
                    click_button2("//button[@aria-label='Add Another Work Experience' and @data-automation-id='Add Another']", self.driver)
                    time.sleep(3)
        except Exception as e:
            print("Error in adding experience.")
            print(e)
        finally:
            print("Done...\n")

    def fill_education_slots(self):
        try:
            print("Adding education, total entries %r." % len(self.data_education))
            click_button2("//button[@aria-label='Add Education' and @data-automation-id='Add']", self.driver)
            time.sleep(2)
            
            for i in range(len(self.data_education)):
                education = self.data_education[i+1]
                education_xpath = f"//div[@data-automation-id='education-{i+1}']"
                
                static_input(f"{education_xpath}//input[@data-automation-id='school']", education['school'], self.driver)
                simple_drop_down(f"{education_xpath}//button[@data-automation-id='degree']", f"//li[@data-value='{education['degree']}']", self.driver)
                
                container = f"{education_xpath}//div[@data-automation-id='multiSelectContainer']"
                input_box = "input[data-automation-id='searchBox']"
                search_query = education['field']
                item_element_id = "//div[@data-automation-label='Computer Science']"
                complex_drop_down(container, input_box, search_query, item_element_id, self.driver)
            
                static_input(f"{education_xpath}//input[@data-automation-id='gpa']", education['gpa'], self.driver)
                
                from_month_element_id = f"{education_xpath}//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionYear-display']"
                to_month_element_id = f"{education_xpath}//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionYear-display']"
                fill_date_widget(from_month_element_id, to_month_element_id, education['from'], education['to'], self.driver)
                
                time.sleep(2)
                if i < len(self.data_education) - 1:
                    click_button2("//button[@aria-label='Add Another Education' and @data-automation-id='Add Another']", self.driver)
        except Exception as e:
            print("Error in adding education.")
            print(e)
        finally:
            print("Done...\n")


    def fill_language_slots(self):
        try:
            print("Adding languages")
            click_button2("//button[@aria-label='Add Languages' and @data-automation-id='Add']", self.driver)
            time.sleep(2)

            for i in range(len(self.data_lang)):
                language = self.data_lang[i+1]
                language_xpath = f"//div[@data-automation-id='language-{i+1}']"
                simple_drop_down(f"{language_xpath}//button[@data-automation-id='language']", f"//li[@data-value='{language['language']}']", self.driver)
                simple_drop_down(f"{language_xpath}//button[@data-automation-id='languageProficiency-0']", f"//li[@data-value='{language['proficiency']}']", self.driver)

                if i < len(self.data_lang) - 1:
                    click_button2("//button[@aria-label='Add Another Languages' and @data-automation-id='Add Another']", self.driver)
        except Exception as e:
            print("Error in adding languages.")
            print(e)
        finally:
            print("Done...\n")

    def add_skills(self):
        try:
            print("Adding skills")
            container = "//div[@data-automation-id='skillsSection']//div[@data-automation-id='multiSelectContainer']"
            input_box = "input[data-automation-id='searchBox']"

            search_list = {"Software": 'Software Applications', "Programming": 'Computer Programming', "Cloud": 'Cloud Computing', "full stack": 'Full Stack Development'}
            complex_drop_down_skills(container, input_box, search_list, self.driver)
        except Exception as e:
            print("Error in adding skills.")
            print(e)
        finally:
            print("Done...\n")

    def add_CV(self):
        try:
            print("Adding CV")
            time.sleep(1)
            add_CV_to_dropbox("//input[@data-automation-id='file-upload-input-ref']", self.cv_file_path, self.driver)
        except Exception as e:
            print("Error in adding CV.")
            print(e)
        finally:
            print("Done...\n")

    def press_submit_button(self):
        try:
            print("Pressing button.")
            click_button2("//button[@data-automation-id='bottom-navigation-next-button']", self.driver)
        except Exception as e:
            print("Error pressing button.")
            print(e)
        finally:
            print("Done...\n") 

