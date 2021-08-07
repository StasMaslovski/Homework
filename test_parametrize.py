import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def ans():
    answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895"])
def test_1(browser, number):
    link = f'https://stepik.org/lesson/{number}/step/1'
    browser.get(link)
    form = browser.find_element_by_tag_name('textarea')
    form.send_keys('123')
    submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
    submit.click()
    # browser.find_element_by_tag_name('button').click()
    # form.submit()
    time.sleep(230)
    ans()


