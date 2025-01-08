import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_1(driver):

    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
               )

    input_field = driver.find_element(By.NAME, 'first-name')
    input_field.send_keys("Иван")

    input_field = driver.find_element(By.NAME, 'last-name')
    input_field.send_keys("Петров")

    input_field = driver.find_element(By.NAME, 'address')
    input_field.send_keys("Ленина, 55-3")

    input_field = driver.find_element(By.NAME, 'e-mail')
    input_field.send_keys("test@skypro.com")

    input_field = driver.find_element(By.NAME, 'phone')
    input_field.send_keys("+7985899998787")

    input_field = driver.find_element(By.NAME, 'city')
    input_field.send_keys("Москва")

    input_field = driver.find_element(By.NAME, 'country')
    input_field.send_keys("Россия")

    input_field = driver.find_element(By.NAME, 'job-position')
    input_field.send_keys("QA")

    input_field = driver.find_element(By.NAME, 'company')
    input_field.send_keys("SkyPro")

    blue_button = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-'
                                      'outline-primary mt-3"]')

    blue_button.click()

    assert "danger" in driver.find_element(By.ID, "zip-code"
                                           ).get_attribute("class")

    fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city',
              'country', 'job-position', 'company']

    for field in fields:
        assert "success" in driver.find_element(By.ID, field
                                                ).get_attribute("class")

    driver.quit()
  
