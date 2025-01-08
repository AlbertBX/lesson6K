import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_3(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    input_field = driver.find_element(By.ID, 'user-name')
    input_field.send_keys("standard_user")

    input_field = driver.find_element(By.ID, 'password')
    input_field.send_keys("secret_sauce")

    driver.find_element(By.ID, 'login-button').click()

    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.ID, 'shopping_cart_container').click()
    driver.find_element(By.ID, 'checkout').click()

    input_field = driver.find_element(By.ID, 'first-name')
    input_field.send_keys("Хакимов")
    input_field = driver.find_element(By.ID, 'last-name')
    input_field.send_keys("Альберт")
    input_field = driver.find_element(By.ID, 'postal-code')
    input_field.send_keys(453100)

    driver.find_element(By.ID, 'continue').click()

    total = driver.find_element(
        By.CSS_SELECTOR, 'div[class="summary_total_label"]').text

    print(total)

    assert total == "Total: $58.29"
    driver.quit()
  
