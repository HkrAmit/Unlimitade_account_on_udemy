import time, random, string
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

link = "https://www.udemy.com/join/signup-popup/"
fullname = "Rayhan Khan" #User Name
def emails():
    return ''.join(random.sample(string.ascii_lowercase, 10)) #Generate Rnadom String for E-mail
paswrd = "Unlmtd_accnt0012" #Password Of the Account
accounts = open("accounts.txt","a")

options=Options()
options.headless=True
browser=webdriver.Firefox(options=options, executable_path = r'/root/Desktop/Automation/Unlimitade_account/bin/geckodriver')

for i in range(100):   # In range set how many accounts you want to create
    try:
        browser.get(link)

        #Fillup Name box
        name = browser.find_element_by_name("fullname")
        name.send_keys(fullname)
        time.sleep(2)

        #Fillup E-mail box with randomly generated fake email
        email = browser.find_element_by_name("email")
        eml = emails()+"@gmail.com"
        email.send_keys(eml)

        #Fillup Password box
        password = browser.find_element_by_name("password")
        password.send_keys(paswrd)

        #Tick the Checkbox
        tick = browser.find_element_by_class_name("checkbox-label").click()

        #Submit and create the account
        submit = browser.find_element_by_name("submit").click()
        time.sleep(3)
        print("Account Created\nEmail: {}\nPassword: {}\n".format(eml, paswrd))

        #Logout Of the new created account
        browser.get("https://www.udemy.com/user/logout/")

        accounts.write("Email: {} Password: {}\n".format(eml, paswrd)) #Save the accounts to this file
    except Exception as e:
        pass

browser.quit()
