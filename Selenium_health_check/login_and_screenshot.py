from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

_URL = ''
_USER_ID = ''
_PWD = ''
_WAIT_TIME_FOR_PUSH = 20
_WAIT_TIME_FOR_SCREENSHOT = 20

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)


def login_and_screenshot():
    try:
        # hit the url
        print("Hitting the page")
        driver.get(_URL)

        # Get the userid control and enter value
        text_id = driver.find_element_by_id('userNameInput')
        text_id.send_keys(_USER_ID)

        # Get the password control and enter value
        text_pass = driver.find_element_by_id('passwordInput')
        text_pass.send_keys(_PWD)

        # Get the submit button control and click it
        btn_submit = driver.find_element_by_id('submitButton')
        print("Entered credentials, trying to login")
        btn_submit.click()

        # We should be on the Duo authentication screen now. find the Push Notification button and click it
        driver.switch_to.frame('duo_iframe')
        btn_send_push = driver.find_element_by_xpath('//button[normalize-space() ="Send Me a Push"]')
        "Reached DUO authentication, sending a push notification"
        btn_send_push.click()

        # Wait for human to approve the push notification
        print(f"Waiting for {_WAIT_TIME_FOR_PUSH} seconds for a human to accept push notification")
        time.sleep(_WAIT_TIME_FOR_PUSH)

        # We should be on the role selection screen with Last used selected by default. click on the login
        btn_login = driver.find_element_by_id("loginButton-btnInnerEl")
        print("Reached role selection page, trying to login")
        btn_login.click()

        # We should be on Price plan screen.
        print(f"Waiting for {_WAIT_TIME_FOR_SCREENSHOT} seconds for screen to load before screenshot")
        time.sleep(_WAIT_TIME_FOR_SCREENSHOT)
        print("**Makes camera sound**")
        driver.save_screenshot('screenshot.png')
    except NoSuchElementException:
        print("SAML Validation failed. try again manually")
        print("Screenshot of error")
        driver.save_screenshot('screenshot.png')
        raise NoSuchElementException
    finally:
        driver.close()


if __name__ == '__main__':
    login_and_screenshot()
