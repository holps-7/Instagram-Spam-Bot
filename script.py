#script.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import jokes

class InstaScript:
    def __init__(self, username, password, victim_username, number):
        self.username = username
        self.password = password
        self.victim_username = victim_username
        self.number = number
        self.browser = webdriver.Firefox()

    def login(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #opening instagram.com
        browser.get('https://www.instagram.com/')
        #-------login process starts
        #finding input boxes for username and password and pasing the appropriate values
        browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        #findind login button and clicking it
        browser.find_element_by_xpath("//button[@type='submit']").click()
        #-------login process ends

    def victim_profile(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #Clicking "Not Now" in pop up just after login
        sleep(2.5)
        not_now_button = browser.find_element_by_xpath("//button[text()='Not Now']")
        sleep(1)
        not_now_button.click()


        #-------search for victim's username starts
        #click search bar
        browser.find_element_by_xpath("//span[text()='Search']").click()
        #enter victim's username and clicking Search
        browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(self.victim_username)
        sleep(1)
        #open victim's profile
        browser.find_element_by_xpath("//span[text()='"+self.victim_username+"']").click()
        sleep(2)
        #-------search for username stops

    def spamming(self):
        browser = self.browser
        browser.implicitly_wait(5)

        #-------spamming begins
        #click message buttom
        browser.find_element_by_xpath("//button[@type='button']").click()
        #input random messages 100 times
        message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
        message_area.click()
        message_area.send_keys("Revenge, the sweetest morsel to the mouth that ever was cooked in hell.", Keys.ENTER)
        for i in range(0, self.number):
            message_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
            message_area.click()
            message_area.send_keys(jokes.get_msg(), Keys.ENTER)

        browser.close()



if __name__ == '__main__':
        Instagram_Spam_Bot = InstaScript('<Username>', '<Password>', 'victim_username', <Number of messages to be spammed>)
        Instagram_Spam_Bot.login()
        Instagram_Spam_Bot.victim_profile()
        Instagram_Spam_Bot.spamming()
