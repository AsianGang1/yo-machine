from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Requires Stackoverflow Account signed in with google and chromedriver
# Replace *PWD* and *EMAIL* with your password and email
# Replace *CHROMEDRIVERPATH* with the path to your chromedriver

# Get chat name

chat_name = input("What's the name of the chat you'd like to spam? ")

# Get Browser set up with chrome
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(options=options,
                           executable_path=r"*CHROMEDRIVERPATH*")

# Login to Stackoverflow through Google
browser.get('https://stackoverflow.com/users/login')
google_button = browser.find_element_by_class_name('s-btn__google')
google_button.click()

# Get email
email_elem = browser.find_element_by_id('identifierId')
email_elem.send_keys('*EMAIL*')

# Go to next
next_button = browser.find_element_by_id('identifierNext')
next_button.click()

# Get password
while True:
    try:
        pwd_elem = browser.find_element_by_css_selector('input[type = "password"]')
        pwd_elem.send_keys('*PWD*')
        break
    except:
        # Accounts for latency
        time.sleep(1)

# Go to next
next_button = browser.find_element_by_id("passwordNext")
next_button.click()

# Switch to Hangouts
while True:
    try:
        browser.execute_script('''window.open("https://hangouts.google.com/", "_blank");''')
        browser.switch_to.window(browser.window_handles[-1])
        break
    except:
        time.sleep(1)
refreshed = False
while True:
    try:
        # Select chat
        browser.switch_to.frame(browser.find_elements_by_class_name('Xyqxtc')[0])
        yangster = browser.find_element_by_css_selector('div[title="' + chat_name + '"]')
        yangster.click()
        break
    except:
        # Check for browser refresh to allow access
        if not refreshed:
            browser.refresh()
            refreshed = True
        time.sleep(4)

# exit chat selector
browser.switch_to.default_content()

# Go to chat window textbox
browser.switch_to.frame(browser.find_elements_by_class_name("Xyqxtc")[1])
chat_box = browser.find_element_by_css_selector("div[class='vE dQ editable']")

# Spam
while True:
    chat_box.send_keys('yoooo')
    chat_box.send_keys(Keys.ENTER)
    time.sleep(0.05)

# CMD: Close all driver tasks = taskkill /f /im chromedriver.exe
