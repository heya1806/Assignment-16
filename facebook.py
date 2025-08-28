from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.get('http://www.facebook.com')
driver.maximize_window()
time.sleep(2)

email_element = driver.find_element(By.XPATH, "//input[@name = 'email']")
email_element.send_keys('YOUR_EMAIL')

password_element = driver.find_element(By.XPATH, "//input[@name = 'pass']")
password_element.send_keys('YOUR_PASSWORD')

time.sleep(2)

login_button = driver.find_element(By.NAME, "login")
login_button.click()

time.sleep(10)

home_button = driver.find_element(By.XPATH, "//a[@aria-label = 'Home']")
home_button.click()
time.sleep(3)

status_button = driver.find_element(By.XPATH, "//span[text() = \"What's on your mind, H?\"]")
status_button.click()
time.sleep(3)

post_text = driver.find_element(By.XPATH, "//div[@role = 'textbox']")
post_text.send_keys('Hi There! From Selenium')
time.sleep(3)

buttons = driver.find_elements(By.XPATH, "//div[@aria-label = 'Post']")
time.sleep(3)
for button in buttons:
    if button.text == "Post":
        button.click()
time.sleep(5)

