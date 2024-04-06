from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time
import json

def save_session_cookies(cookies_file_path, driver):
    cookies = driver.get_cookies()
    with open(cookies_file_path, 'w') as file:
        json.dump(cookies, file)
        print('Session has been successfully saved')

def scroll_to_element(element, driver):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(1)

def scroll_to_bottom_then_top(driver):
    try:
        print("Scrolling to the bottom of the page...")
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
        time.sleep(3)
        print("Scrolling back to the top of the page...")
        driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
        time.sleep(2)
        
    except Exception as e:
        print("Error during scrolling:", e)
    finally:
        print("Scrolling completed.\n")

def static_input(xpath, data, driver):
    static_form = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    scroll_to_element(static_form, driver)
    static_form.clear() 
    static_form.send_keys(data)

def radial_input_no(element_id, radial_id, label, driver):
    radio_group = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"div[data-automation-id='{element_id}']"))
    )
    
    # Find the label that contains "No"
    no_label = radio_group.find_element(By.XPATH, f"{radial_id}")
    no_input_id = no_label.get_attribute(f'{label}')
    no_radio_button = driver.find_element(By.ID, no_input_id)
    no_radio_button.click()

def simple_drop_down(element_id, list_item_id, driver):
    retries = 3  
    for _ in range(retries):
        try:
            dropdown_menu = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, element_id))
            )
            scroll_to_element(dropdown_menu, driver)
            time.sleep(1)
            dropdown_menu.click()

            list_item = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, list_item_id))
            )
            #scroll_to_element(list_item, driver)
            #time.sleep(1)
            list_item.click()
            break  
        except StaleElementReferenceException:
            continue  

def complex_drop_down(container_id, element_id, text_input, list_item_id, driver):

    # Focus the menu container
    widget_activation_area = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"{container_id}"))
    )
    scroll_to_element(widget_activation_area, driver)
    time.sleep(1) 
    ActionChains(driver).move_to_element(widget_activation_area).click().perform()

    # Focus the element
    search_input_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"{element_id}"))
    )
    search_input_box.click()  

    # Type in the input box
    search_input_box.send_keys(f"{text_input}")
    search_input_box.send_keys(Keys.RETURN) 
    
    # Wait for dropdown to populate and options to be visible
    # Adjust the selector based on the actual dropdown items' HTML attributes
    dropdown_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"{list_item_id}"))
    )
    time.sleep(2)
    dropdown_option.click() 

def complex_drop_down_skills(container_id, element_id, word_list, driver):
    widget_activation_area = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"{container_id}"))
    )
    scroll_to_element(widget_activation_area, driver)
    time.sleep(1) 
    ActionChains(driver).move_to_element(widget_activation_area).click().perform()

    for key, value in word_list.items():
        search_input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"{element_id}"))
        )
        search_input_box.click()  

        search_input_box.send_keys(key)
        search_input_box.send_keys(Keys.RETURN) 

        dropdown_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-automation-label='{value}']"))
        )
        time.sleep(2)
        dropdown_option.click() 

def click_button(element_id, driver):
    click_filter_div = driver.find_element(By.CSS_SELECTOR, f'div[data-automation-id="{element_id}"]')
    driver.execute_script("arguments[0].click();", click_filter_div)

def click_button2(element_xpath, driver):
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, element_xpath))
    )
    scroll_to_element(button, driver)
    time.sleep(1)
    button.click()

def fill_date_widget(month_element, year_element, month, year, driver):
    get_from_month_element = driver.find_element_by_xpath(month_element)
    get_from_year_element = driver.find_element_by_xpath(year_element)
    driver.execute_script("arguments[0].innerText = arguments[1];", get_from_month_element, month)
    driver.execute_script("arguments[0].innerText = arguments[1];", get_from_year_element, year)

def add_CV_to_dropbox(input_element, path, driver):
    file_input = driver.find_element_by_xpath(input_element)
    file_input.send_keys(path)

