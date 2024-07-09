import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

webhook_url = "https://discord.com/api/webhooks/1260028702834688011/BlpeEFYqZCs1zB-7FcWV871-DRxiy4Lcwv6WqIWcSM6VnqY8dlGfFlYAm-6f__STgSjb"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument(r"--profile-directory=Profile 4")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://best-links.org/s?94406c67")

    button_css_selector = '.sdfdsahps'
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, button_css_selector)))
    driver.find_element(By.CSS_SELECTOR, button_css_selector).click()

    
    end_time = time.time() + 120

    while time.time() < end_time:
        try:
            
            done_button_xpath = '//div[contains(text(), "Done >")]'
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, done_button_xpath))).click()
            time.sleep(1)
        except:
            pass

        if driver.current_url != "https://best-links.org/s?94406c67":
            message = f"bypass Successful: {driver.current_url}"
            payload = {"content": message}
            requests.post(webhook_url, json=payload)
            break

finally:
    driver.quit()