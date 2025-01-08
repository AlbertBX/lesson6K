import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_2(driver):
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    input_field = driver.find_element(By.ID, 'delay')

    input_field.clear()

    input_field.send_keys(45)

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    result = WebDriverWait(driver, 45).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div[class="screen"]'))).text
    print(result)
    assert result == "15"

    driver.quit()
    
