from selenium.common.exceptions import NoSuchElementException

import email_with_attachment as e
import login_and_screenshot as l

try:
    print("Trigger login and screenshot")
    l.login_and_screenshot()

    print("trigger email with attachment")
    e.email_with_attachment()
except NoSuchElementException:
    print("Looks like SAML ERROR")
    e.email_with_attachment('Failed')