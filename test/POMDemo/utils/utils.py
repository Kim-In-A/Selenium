# This base class will be for credentials and hooks/reusable methods

import inspect

#4C Insight Credentials
URL_4CInsights = "https://www.4cinsights.com"
USERNAME_4CInsights = "123@gmail.com"
PASSWORD_4CInsight = "123456"


 #Gmail account creating credentials
URL_gmail ="https://accounts.google.com/signup/v2"
FIRST_NAME= "ABC"
LAST_NAME = "ABCE"
USERNAME_GMAIL = "123ABDSC"
PASSWORD_GMAIL = "12ABCD2341"
PHONE_NUMBER = "123456789"


# This method will save screenshot of the webpage
def save_screenshot(driver, name):
    driver.get_screenshot_as_file("/Users/ritakk/frameWork/test/POMDemo/reports" + name + "image/png")
