from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

driver = webdriver.Chrome('G:/Project/Instagram_Scrapper/chromedriver.exe')
driver.get("https://mbasic.facebook.com/")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

username.clear()
password.clear()
username.send_keys("*--")
password.send_keys("00")

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login/save-device/cancel/?flow=interstitial_nux&nux_source=regular_login']"))).click()

driver.get("https://mbasic.facebook.com/friends/center/friends/?mff_nav=1")
condition = True
name_list = []
# info_list = []
# friends_list = []
while condition:
    friends_names = driver.find_elements_by_xpath("//td[@style='vertical-align: middle']//a[contains(text(),'')]")
    for friend in friends_names:
        name_list.append(friend.text)
    # extra_infos = driver.find_elements_by_xpath("//td[@style='vertical-align: middle']//a[contains(text(),'')]//following-sibling::div")
    # for extra_info in extra_infos:
    #     info_list.append(extra_info.text)
    # friends_list.append([name_list, info_list])
    try:
        see_more = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'See More')]//parent::a"))).click()
    except:
        condition = False

for name in name_list:
    print(name)

# friends_mutual = driver.find_elements_by_xpath("//div[contains(text(),'mutual friends')]")
# friends_mutual = [mutual_friends.text for mutual_friends in friends_mutual]

# for x in range(0, len(name_list)):
#     for y in range(0, len(info_list)):
#         print(friends_list[x], [y])
    # friend_name.click()
    # profiles_url = driver.find_elements_by_xpath(" //span[text()='View Profile']//parent::a")
    # profiles_url = [profile_url.get_attribute('href') for profile_url in profiles_url]
    # for profile_url in profiles_url:
    #     print(profile_url)


    # profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'View Profile')]//parent::a[contains(text(),'')]"))).click()
    # about = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='About']"))).click()
    #
    # contacts = driver.find_elements_by_xpath("//div[@id='contact-info']//div[contains(text(),'')]//div[contains(text(),'')]//following-sibling::div[contains(text(),'')]")
    # contacts = [contact.get_attribute('td') for contact in profiles_url]
    # for contact in contacts:
    #     print(contact)










# while True:
#
#
#
#
#
#     see_more = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#         (By.XPATH, "//span[text()='See More']//parent::a"))).click()







