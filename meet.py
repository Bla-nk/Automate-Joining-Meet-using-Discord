import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

opt=Options()
opt.add_experimental_option("prefs", {
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 2,
"profile.default_content_setting_values.notifications": 1
})
sub=0
def meetjoin():
    browser = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\91748\Downloads\chromedriver')
    browser.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(7)
    email = browser.find_element_by_xpath("//*[@id='identifierId']")
    time.sleep(2)
    email.send_keys('shivanshuminz_2k19ec181@dtu.ac.in', Keys.ENTER)
    time.sleep(5)
    # NEXT button
    # browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    # password
    password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    time.sleep(5)
    password.send_keys('Bub@Bubba047', Keys.ENTER)
    time.sleep(5)

    browser.get(sub)