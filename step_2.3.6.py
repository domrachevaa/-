from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def cal(int_):
    return str(math.log(abs(12 * math.sin(int(int_)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    new = browser.window_handles[1]
    browser.switch_to.window(new)

    x = browser.find_element_by_css_selector("span#input_value")\
        .text
    browser.find_element_by_css_selector("input#answer")\
        .send_keys(
        cal(x)
        )
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(40)
    browser.quit()
