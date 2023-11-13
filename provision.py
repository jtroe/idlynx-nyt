import os

library = os.environ.get('LIBRARY_NAME', 'Meridian Library District')
library_card_number = os.environ.get('LIBRARY_CARD_NUMBER', '').strip()
if len(library_card_number) < 14:
    raise ValueError("Library card number must be 14 digits")
nyt_username = os.environ.get('NYT_USERNAME', '').strip()
nyt_password = os.environ.get('NYT_PASSWORD', '').strip()

form_url = "https://form.jotform.com/220755446894164"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# create a new Chrome session
driver = webdriver.Chrome()

# navigate to the form URL
driver.get(form_url)

driver.find_element(By.ID, "input_10").send_keys(library)
driver.find_element(By.ID, "input_6").send_keys(library_card_number[:7])
driver.find_element(By.ID, "input_7").send_keys(library_card_number[-7:])

# submit the form
driver.find_element(By.ID, 'input_8').click()

# print the current URL
print(driver.current_url)

driver.find_element(By.CLASS_NAME, "giftRedeem__submitButton").click()

# wait for up to 15 seconds for the element with id 'email' to become available
email_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'email')))
email_field.send_keys(nyt_username)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# wait for up to 15 seconds for the element with id 'password' to become available
password_field = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'password')))
password_field.send_keys(nyt_password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)