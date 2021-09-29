from selenium import webdriver
import time
import unittest


class test_unitest_style(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        inp1 = browser.find_element_by_xpath(
            "//label[contains(text(), '*')]/following-sibling::input[@class='form-control first']")
        inp1.send_keys("Purr")
        inp2 = browser.find_element_by_xpath(
            "//label[contains(text(), '*')]/following-sibling::input[@class='form-control second']")
        inp2.send_keys("Purrington")
        inp3 = browser.find_element_by_xpath(
            "//label[contains(text(), '*')]/following-sibling::input[@class='form-control third']")
        inp3.send_keys("purr@mail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "")
        browser.quit()

    def test_second(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        inp1 = browser.find_element_by_xpath(
            "//label[contains(text(), '*')]/following-sibling::input[@class='form-control first']")
        inp1.send_keys("Purr")
        inp2 = browser.find_element_by_xpath(
            "//label[contains(text(), '*')]/following-sibling::input[@class='form-control second']")
        inp2.send_keys("Purrington")
        inp3 = browser.find_element_by_xpath(
            "//label[contains(text(), '*')]/following-sibling::input[@class='form-control third']")
        inp3.send_keys("purr@mail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
