from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_dynamic_xpath():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    time.sleep(5)

    # Find element
    courses = driver.find_element(By.XPATH, "//a[contains(@href,'courses')]")

    # Parent
    parent = courses.find_element(By.XPATH, "..")
    print("Parent:", parent.tag_name)

    # First child
    first_child = parent.find_element(By.XPATH, "./*")
    print("First child:", first_child.tag_name)

    # Second sibling
    siblings = parent.find_elements(By.XPATH, "./following-sibling::*")
    if len(siblings) >= 2:
        print("Second sibling:", siblings[1].text)

    # Parent of href element
    href_element = driver.find_element(By.XPATH, "//a[@href]")
    href_parent = href_element.find_element(By.XPATH, "..")
    print("Parent of href:", href_parent.tag_name)

    # Axes
    ancestors = courses.find_elements(By.XPATH, "./ancestor::*")
    print("Ancestors:", len(ancestors))

    following = courses.find_elements(By.XPATH, "./following-sibling::*")
    print("Following siblings:", len(following))

    preceding = courses.find_elements(By.XPATH, "./preceding::*")
    print("Preceding elements:", len(preceding))

    driver.quit()


test_dynamic_xpath()