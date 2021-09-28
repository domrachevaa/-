from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def cal(int_):
    return str(math.log(abs(12 * math.sin(int(int_)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_tag_name("button")\
        .click()
    x = browser.find_element_by_css_selector("span#input_value") \
        .text
    browser.find_element_by_css_selector("input#answer") \
        .send_keys(
        cal(x)
    )
    browser.find_element_by_css_selector("button#solve").click()

finally:
    time.sleep(40)
    browser.quit()