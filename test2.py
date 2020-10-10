from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
import time

email = "knpkaa@gmail.com"
password = "sY2d$J#!JsEAK7Iu5bwkM*Z5!T&fX"

driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(driver)
chrome_browser.maximize_window()
# z = int(input('How Much pages to parse? there is max 17 pages '))

url = 'https://couponscorpion.com/category/100-off-coupons/'

rawUrl = requests.get(url).text
soup = BeautifulSoup(rawUrl, 'html.parser')
# link1 = soup.find_all(
#     'div', {"class": 'newsdetail newstitleblock rh_gr_right_sec'})
# for link in link1:
#     print(link['href'])
# pprint(link1)


links = []
for div in soup.find_all(
        'div', {"class": 'newsdetail newstitleblock rh_gr_right_sec'}):
    for a in div.select('a'):
        links.append(a['href'])


pprint(f'{links}================ raw links above ============')
# Get scorpion links and afet get LIST of links directly to courses


def reedemCourse(url):

    chrome_browser.get("https://www.udemy.com/join/login-popup/")

    email = chrome_browser.find_element_by_name("email")
    password = chrome_browser.find_element_by_name("password")

    email.send_keys(email_text)
    password.send_keys(password_text)

    chrome_browser.find_element_by_name("submit").click()

    chrome_browser.get(url)
    print("Trying to Enroll for: " + chrome_browser.title)

    # Enroll Now 1
    element_present = EC.presence_of_element_located(
        (By.XPATH, "//button[@data-purpose='buy-this-course-button']"))
    WebDriverWait(chrome_browser, 10).until(element_present)

    udemyEnroll = chrome_browser.find_element_by_xpath(
        "//button[@data-purpose='buy-this-course-button']")  # Udemy
    udemyEnroll.click()

    # Enroll Now 2
    element_present = EC.presence_of_element_located(
        (By.XPATH, "//*[@id=\"udemy\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button"))
    WebDriverWait(chrome_browser, 10).until(element_present)

    # Assume sometimes zip is not required because script was originally pushed without this
    try:
        zipcode_element = chrome_browser.find_element_by_id(
            "billingAddressSecondaryInput")
        zipcode_element.send_keys(zipcode)

        # After you put the zip code in, the page refreshes itself and disables the enroll button for a split second.
        time.sleep(1)
    except NoSuchElementException:
        pass

    udemyEnroll = chrome_browser.find_element_by_xpath(
        "//*[@id=\"udemy\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button")  # Udemy
    udemyEnroll.click()


def getUdemyPhpLinks(links):
    udemy_php_links = []
    for link in links:
        chrome_browser.get(link)
        time.sleep(5)
        chrome_browser.find_element_by_xpath(
            '//button[@class="align-right primary slidedown-button"]').click()
        content = chrome_browser.page_source
        soup = BeautifulSoup(content, 'html.parser')
        course_link = soup.find_all('span', {'class': "rh_button_wrapper"})
        for i in course_link:
            phplink = i.find('a', href=True)
            if phplink is None:
                print('No Links Found')
        reedemCourse(phplink)


getUdemyPhpLinks(links)

# go to udemy courses from list of links and click add button if FREE

# after a page click card and enroll if card cost == 0

# repeat so many times as pages entered
