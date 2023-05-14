from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Firefox()

users = ['Username']
message = "This message is sent using Instagram Bot."


class bot:
  
    def __init__(self, username, password, user, message):
        
        # initializing the username
        self.username = username
          
        # initializing the password
        self.password = password
          
        # passing the list of user or initializing
        self.user = user
          
        # passing the message of user or initializing
        self.message = message
          
        # initializing the base url.
        self.base_url = 'https://www.instagram.com/'
          
        # here it calls the driver to open chrome web browser.
        self.bot = driver
          
        # initializing the login function we will create
        self.login()

    def login(self):
  
        self.bot.get(self.base_url)
        
        # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
    
        enter_username.send_keys(self.username)
        
        # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
    
        # RETURNING THE PASSWORD and login into the account
        enter_password.send_keys(Keys.RETURN)
        time.sleep(15)

        self.bot.find_element("xpath","//button[text()='Not Now']").click()
        time.sleep(4)
        self.bot.find_element("xpath","//button[text()='Not Now']").click()
        time.sleep(4)

        self.bot.find_element("xpath","//a[@href='/direct/inbox/']").click()
        time.sleep(10)
        
        for i in users:

            self.bot.find_element("xpath","//button[@class='_abl- _abm2']").click()
            time.sleep(10)
  
            # enter the username
            self.bot.find_element("css selector","input[name='queryBox']").send_keys(i)
            time.sleep(2)

            # click on the username
            # WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located((By.XPATH, "//div[@class='_abm0']")))
            WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='_abl-']"))).click()
            time.sleep(2)
        
            # next button
            self.bot.find_element("xpath","//div[text()='Next']").click()
            time.sleep(5)
        
            # click on message area
            send = self.bot.find_element("xpath",'//textarea')
        
            # types message
            send.send_keys(self.message)
            time.sleep(1)
        
            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(5)

def init():
    username = input('Enter the username: ')
    password = input('Enter your password: ')
    bot(username, password, users, message)
    
    # when our program ends it will show "done".
    print("DONE")
  
  
# calling the function
init()

