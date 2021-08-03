from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(d):
    return str(math.log(abs(12 * math.sin(int(d)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button = browser.find_element_by_id('book').click()
form = browser.find_element_by_id('answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", form)
number = browser.find_element_by_id('input_value').text
result = calc(number)

form.send_keys(result)
form.submit()
