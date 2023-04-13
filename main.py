from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv.main import load_dotenv
import os
import time

chrome_driver_path = r"C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)

load_dotenv()
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3560002608&f_AL=true&f_E=1%2C2&geoId=105773754&keywords=python%20developer&location=Bucharest%2C%20Romania&refresh=true"
my_email = os.environ["MY_EMAIL"]
account_password = os.environ["LNKD_PASSWORD"]
my_phone_num = os.environ["PHONE_NUM"]

driver.get(URL)
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(2)
user_name = driver.find_element(By.ID, "username")
user_name.send_keys(my_email)
password = driver.find_element(By.ID, "password")
password.send_keys(account_password)
password.send_keys(Keys.ENTER)

time.sleep(3)
# store current window (browser tab) id, that will help us in final step, wait for that.
main_window_id = driver.current_window_handle

# create list of all the jobs available on current page
search_results = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
for job in search_results:
    job.click()
    time.sleep(2)
    try:
        # to locate the apply button, if it can't be located, skip the job
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()
        time.sleep(5)
        submit_button = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button .artdeco-button__text")
        # if submit button is available in page, only then fill the form, otherwise it has multi steps to fill form.
        if submit_button.text == 'Submit application':
            phone_number = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text input")
            # check if the text field is empty, only then enter your number
            if phone_number.text == "":
                phone_number.send_keys(my_phone_num)
            submit_button.click()
            print("Application submitted.")
            time.sleep(5)
            try:
                # after submitting form, click x to close the confirmation banner (either this will occur)
                x_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss svg")
                x_button.click()
            except NoSuchElementException:
                # after submission, sometimes there comes another pop-up that we need to close as well
                # (or this will occur)
                click_dismiss = driver.find_element(By.CSS_SELECTOR, '.artdeco-toast-item__dismiss svg')
                click_dismiss.click()
        else:
            # in-case the submit button isn't available go back to the main menu using below steps
            x_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss svg")
            x_button.click()
            time.sleep(2)
            discard_btn = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[0]
            # 0 to discard, 1 to save for later
            discard_btn.click()

    except NoSuchElementException:
        continue
    finally:
        time.sleep(2)
        all_windows = driver.window_handles   # creates list of all opened browser tab id's
        for tab_id in all_windows:
            if tab_id != main_window_id:
                driver.switch_to.window(tab_id)
                driver.close()   # close all tabs except the one which we want(jobs main page)
        # if we click on apply, it will take us to another window, so this step will redirect us to the original page.
        driver.switch_to.window(main_window_id)
        time.sleep(3)


time.sleep(5)
driver.quit()

