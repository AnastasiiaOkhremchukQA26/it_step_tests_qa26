from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get("https://casenik.com.ua/user/login")

email_field = browser.find_element(By.XPATH, '//input[@id="email"]')
email_field.send_keys("nastia.o0403@gmail.com")
password_field = browser.find_element(By.XPATH, '//input[@id="pasword"]')
password_field.send_keys("12345678")
login_button = browser.find_element(By.XPATH, '//button[@class="btn button-gen"]').click()

message = WebDriverWait(browser, 32).until_not(
    #EC.element_to_be_clickable((By.XPAth, "//div[@class = 'alert alert-success']"))
    EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-success']"))
)
time.sleep(5)


