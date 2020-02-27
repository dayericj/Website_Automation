#**************************************************************************
#Function Name: Driver
#Function Description: Driver component will find and click given link and find elements specified.
#Author: Eric Day
#Date Created: 2/24/2020
#Modified by:
#Modification Date:
#**************************************************************************

import catch as catch
from selenium import webdriver
# ///Saved user name and Password///
from selenium.common.exceptions import NoSuchElementException

# /// UID and PW to be called in a data sheet soon.///
username = 'opensourcecms'
password = 'opensourcecms'

# ///URL and Driver variable defined///


# ///Website to launch///
url = 'https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/auth/login'
driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver_win32/chromedriver")
driver.get(url)

driver.set_page_load_timeout(5)

# /// Input UID and PW and send Click
driver.find_element_by_id("txtUsername").send_keys(username)
driver.find_element_by_id('txtPassword').send_keys(password)
driver.find_element_by_class_name('button').click()

# ///Excception Handling: Confirm that webpage has loaded by finding the identified element
WaitForElement = driver.find_element_by_id('option-menu-bar')
if WaitForElement:

    print('Log in to OrangeHRM was successful')
else:
    print('Login page failed to load')




