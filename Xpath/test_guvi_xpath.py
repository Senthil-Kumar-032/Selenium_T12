from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_guvi_navigation():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    time.sleep(5)

    # Title check
    assert "GUVI" in driver.title

    # Only check element exists (no is_displayed)
    courses = driver.find_element(By.XPATH, "//a[contains(@href,'courses')]")
    assert courses is not None

    driver.quit()


def test_xpath_axes():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    time.sleep(5)

    courses = driver.find_element(By.XPATH, "//a[contains(@href,'courses')]")

    # Ancestors
    ancestors = courses.find_elements(By.XPATH, "./ancestor::*")
    assert len(ancestors) > 0

    # Following siblings
    following = courses.find_elements(By.XPATH, "./following-sibling::*")
    assert len(following) > 0

    driver.quit()