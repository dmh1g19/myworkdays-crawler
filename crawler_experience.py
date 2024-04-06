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
    def __init__(self, driver, data_work_experience, data_education):
        self.driver = driver # Driver should already be instantiated from previous page
        self.data_work_experience = data_work_experience
        self.data_education = data_education

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

            #time.sleep(3)
            #print("Adding experience, total entries %r." % (len(self.data_work_experience)))
            #click_button2("//button[@aria-label='Add Work Experience' and @data-automation-id='Add']", self.driver)
            #time.sleep(3)

            #static_input("//div[@data-automation-id='workExperience-1']//input[@data-automation-id='jobTitle']", self.data_work_experience[1]['job_title'], self.driver)
            #static_input("//div[@data-automation-id='workExperience-1']//input[@data-automation-id='company']", self.data_work_experience[1]['company'], self.driver)
            #static_input("//div[@data-automation-id='workExperience-1']//input[@data-automation-id='location']", self.data_work_experience[1]['location'], self.driver)

            #from_month_element_id = "//div[@data-automation-id='workExperience-1']//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionMonth-display']"
            #from_year_element_id = "//div[@data-automation-id='workExperience-1']//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionYear-display']"
            #fill_date_widget(from_month_element_id, from_year_element_id, self.data_work_experience[1]['from_month'], self.data_work_experience[1]['from_year'], self.driver)

            #to_month_element_id = "//div[@data-automation-id='workExperience-1']//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionMonth-display']"
            #to_year_element_id = "//div[@data-automation-id='workExperience-1']//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionYear-display']"
            #fill_date_widget(to_month_element_id, to_year_element_id, self.data_work_experience[1]['to_month'], self.data_work_experience[1]['to_year'], self.driver)

            #static_input("//div[@data-automation-id='workExperience-1']//textarea[@data-automation-id='description']", self.data_work_experience[1]['description'], self.driver)
            #time.sleep(1)

            #for i in range(1, len(self.data_work_experience)):
            #    click_button2("//button[@aria-label='Add Another Work Experience' and @data-automation-id='Add Another']", self.driver)
            #    time.sleep(3)

            #    static_input("//div[@data-automation-id='workExperience-%r']//input[@data-automation-id='jobTitle']" % (i+1), self.data_work_experience[i+1]['job_title'], self.driver)
            #    static_input("//div[@data-automation-id='workExperience-%r']//input[@data-automation-id='company']" % (i+1), self.data_work_experience[i+1]['company'], self.driver)
            #    static_input("//div[@data-automation-id='workExperience-%r']//input[@data-automation-id='location']" % (i+1), self.data_work_experience[i+1]['location'], self.driver)

            #    from_month_element_id = "//div[@data-automation-id='workExperience-%r']//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionMonth-display']" % (i+1)
            #    from_year_element_id = "//div[@data-automation-id='workExperience-%r']//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionYear-display']" % (i+1)
            #    fill_date_widget(from_month_element_id, from_year_element_id, self.data_work_experience[i+1]['from_month'], self.data_work_experience[i+1]['from_year'], self.driver)

            #    to_month_element_id = "//div[@data-automation-id='workExperience-%r']//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionMonth-display']" % (i+1)
            #    to_year_element_id = "//div[@data-automation-id='workExperience-%r']//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionYear-display']" % (i+1)
            #    fill_date_widget(to_month_element_id, to_year_element_id, self.data_work_experience[i+1]['to_month'], self.data_work_experience[i+1]['to_year'], self.driver)

            #    static_input("//div[@data-automation-id='workExperience-%r']//textarea[@data-automation-id='description']" % (i+1), self.data_work_experience[i+1]['description'], self.driver)

        except Exception as e:
            print("Error in adding experience.")
            print(e)
        finally:
            print("Done...\n")

    def fill_education_slots(self):
        try:
            print("Adding education, total entries %r." % (len(self.data_education)))
            click_button2("//button[@aria-label='Add Education' and @data-automation-id='Add']", self.driver)
            time.sleep(2)

            static_input("//div[@data-automation-id='education-1']//input[@data-automation-id='school']", self.data_education[1]['school'], self.driver)
            simple_drop_down("//div[@data-automation-id='education-1']//button[@data-automation-id='degree']", f"//li[@data-value='{ self.data_education[1]['degree']}']", self.driver)
            
            container = "//div[@data-automation-id='education-1']//div[@data-automation-id='multiSelectContainer']"
            input_box = "input[data-automation-id='searchBox']"
            search_query = self.data_education[1]['field']
            item_element_id = "//div[@data-automation-label='Computer Science']"
            complex_drop_down(container, input_box, search_query, item_element_id, self.driver)
            
            static_input("//div[@data-automation-id='education-1']//input[@data-automation-id='gpa']", self.data_education[1]['gpa'], self.driver)
            
            from_month_element_id = "//div[@data-automation-id='education-1']//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionYear-display']"
            from_year_element_id = "//div[@data-automation-id='education-1']//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionYear-display']"
            fill_date_widget(from_month_element_id, from_year_element_id, self.data_education[1]['from'], self.data_education[1]['to'], self.driver)
            time.sleep(2)

            for i in range(1, len(self.data_education)):
                click_button2("//button[@aria-label='Add Another Education' and @data-automation-id='Add Another']", self.driver)

                static_input("//div[@data-automation-id='education-%r']//input[@data-automation-id='school']" % (i+1), self.data_education[i+1]['school'], self.driver)
                simple_drop_down("//div[@data-automation-id='education-%r']//button[@data-automation-id='degree']" % (i+1), f"//li[@data-value='{self.data_education[i+1]['degree']}']", self.driver)
                
                container = "//div[@data-automation-id='education-%r']//div[@data-automation-id='multiSelectContainer']" % (i+1)
                input_box = "input[data-automation-id='searchBox']"
                search_query = self.data_education[i+1]['field']
                item_element_id = "//div[@data-automation-label='Computer Science']"
                complex_drop_down(container, input_box, search_query, item_element_id, self.driver)

                static_input("//div[@data-automation-id='education-%r']//input[@data-automation-id='gpa']" % (i+1), self.data_education[i+1]['gpa'], self.driver)
                
                from_month_element_id = "//div[@data-automation-id='education-%r']//div[@data-automation-id='formField-startDate']//div[@data-automation-id='dateSectionYear-display']" % (i + 1)
                from_year_element_id = "//div[@data-automation-id='education-%r']//div[@data-automation-id='formField-endDate']//div[@data-automation-id='dateSectionYear-display']" % (i + 1)
                fill_date_widget(from_month_element_id, from_year_element_id, self.data_education[i+1]['from'], self.data_education[i+1]['to'], self.driver)
                
        except Exception as e:
            print("Error in adding education.")
            print(e)
        finally:
            print("Done...\n")


