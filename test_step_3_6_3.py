from selenium import webdriver
import time
import math
import pytest
# страницы которые надо проверить:
'''https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1'''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize(
    'no',
    ["895", "896", "897", "898", "899", "903", "904", "905"]
)
def test_parametrize(browser, no):
    global res
    link = f"https://stepik.org/lesson/236{no}/step/1"
    answer = math.log(int(time.time()))
    browser.get(link)
    browser.implicitly_wait(12)
    browser.find_element_by_css_selector("textarea").send_keys(str(answer))
    browser.find_element_by_css_selector('button[class="submit-submission"]').click()
    text_out = browser.find_element_by_css_selector('pre[class="smart-hints__hint"]').text
    assert "Correct!" == text_out, f"{text_out}"
    res.append(text_out)

