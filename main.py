
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

Username = "your_email" #
Password = "your_linkedin_password" #
phoneNo = "1234567890"
url = "https://www.linkedin.com/jobs/search/?f_AL=true&keywords="

chrome_driver_path = "chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

username_field = driver.find_element_by_id("username")
username_field.send_keys(Username)

password_field = driver.find_element_by_id("password")
password_field.send_keys(Password)
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(3)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        phone_no = driver.find_element_by_css_selector(".fb-single-line-text__input")
        phone_no.send_keys(phoneNo)
        next_button = driver.find_element_by_css_selector("footer button")
        if next_button.get_attribute("data-control-name") == "submit_unify":
            next_button.click()
        elif next_button.get_attribute("data-control-name") == "continue_unify":
            next_button.click()
        review_button = next_button
        if review_button.get_attribute("data-control-name") == "review_unify":
            option_button = driver.find_elements_by_css_selector("form input")
            for optn in option_button:
                if option_button.get_attribute("value") == "yes":
                    option_button.click()
            #
            option1 = driver.find_elements_by_css_selector(".fb-single-line-text__input")
            for opt in option1:
                option1.send_keys("0")
                time.sleep(1)
        review_button.click()
        time.sleep(2)
        submit_button = driver.find_element_by_class_name("artdeco-button--primary")
        if submit_button.get_attribute("data-control-name") == "submit_unify":
            submit_button.click()
            time.sleep(2)
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
        else:
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_xpath("//button[contains(@class, 'artdeco-button')]//*[contains(., 'Discard')]/..")
            discard_button.click()
            print("Complex application, skipped...")
            continue
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
