from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest


def testShouldFireKeyPressEvents(driver, pages):
    pages.load("javascriptPage.html")
    keyReporter = driver.find_element(by=By.ID, value="keyReporter")
    keyReporter.send_keys("a")
    result = driver.find_element(by=By.ID, value="result")
    assert "press:" in result.text