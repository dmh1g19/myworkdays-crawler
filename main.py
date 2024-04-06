from crawler_info import *
from crawler_experience import *
from parse_data import *

driver_path = './chromedriver'
config_file_path = './info.txt'
work_experience_file_path = './work_experience.txt'
edu_file_path = "./education.txt"
cookies_file_path = 'cookies.txt'

#url = input("Provide form link: ")
url = "https://relx.wd3.myworkdayjobs.com/en-US/relx/login?redirect=%2Fen-US%2Frelx%2Fjob%2FParis%2FSales-Development-Representative_R75982-1%2Fapply%2FapplyManually"
#url = "https://workday.wd5.myworkdayjobs.com/en-US/Workday/login?redirect=%2Fen-US%2FWorkday%2Fjob%2FIreland%252C-Dublin%2FSenior-Software-Development-Engineer---Application-Development_JR-0086602%2Fapply%2FapplyManually"
#url = "https://dell.wd1.myworkdayjobs.com/en-US/External/login?redirect=%2Fen-US%2FExternal%2Fjob%2FRemote---United-Kingdom-Scotland%2FIntern-Software-Engineer---Platform-Engineering----100--Remote-UK-_R240901%2Fapply%2FautofillWithResume"

parser = Parser(config_file_path, work_experience_file_path, edu_file_path)
parser.read_config_file()
data = parser.get_data()

parser.read_work_file()
data_work = parser.get_data_work()

parser.read_edu_file()
data_edu = parser.get_data_edu()

crawler_my_info = CrawlerMyInfo(driver_path, data)
crawler_my_info.get_website(url)
crawler_my_info.sign_in()
#crawler_my_info.where_did_you_hear_about_us()
#crawler_my_info.have_you_worked_for_us_before()
#crawler_my_info.select_country()
#crawler_my_info.select_name_prefix()
#crawler_my_info.enter_name_and_surname()
#crawler_my_info.enter_address()
#crawler_my_info.enter_phone()

print("Completed my info section.")
if input("Press enter to move to next section..") == "":
    crawler_my_info.press_submit_button()        

crawler_my_experience = CrawlerMyExperience(crawler_my_info.get_driver(), data_work, data_edu)
crawler_my_experience.fill_experience_slots()
crawler_my_experience.fill_education_slots()

print("Form completed.")
if input("Press enter to kill driver.") == "":
    crawler_my_info.kill_driver()
