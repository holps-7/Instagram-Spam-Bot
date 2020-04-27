from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import jokes

browser = webdriver.Firefox()

browser.implicitly_wait(5)

#opening instagram.com
browser.get('https://www.instagram.com/')

#-------login process starts
#finding input boxes for username and password
username_input = browser.find_element_by_xpath("//input[@name='username']")
password_input = browser.find_element_by_xpath("//input[@name='password']")
#parsing value for username and password
username_input.send_keys("USERNAME")
password_input.send_keys("PASSWORD")
#findind login button and clicking it
browser.find_element_by_xpath("//button[@type='submit']").click()
#-------login process ends



#Clicking "Not Now" in pop up just after login
sleep(2.5)
not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
sleep(1)
not_now_button.click()



#-------search for victim's username starts
#click search bar
browser.find_element_by_xpath("//span[text()='Search']").click()
#enter victim's username and clicking Search
browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys("VICTIM_USERNAME")
sleep(1)
#open victim's profile
browser.find_element_by_xpath("//span[text()='VICTIM_USERNAME']").click()
sleep(2)
#-------search for username stops



#-------spamming begind
#click message buttom
browser.find_element_by_xpath("//button[@type='button']").click()
#input random messages 100 times
message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
message_area.click()
message_area.send_keys("Revenge, the sweetest morsel to the mouth that ever was cooked in hell.", Keys.ENTER)
for i in range(0, 100):
    message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
    message_area.click()
    message_area.send_keys(jokes.get_msg(), Keys.ENTER)

browser.close()
