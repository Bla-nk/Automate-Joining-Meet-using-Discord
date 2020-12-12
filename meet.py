import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
with open('id-pass.json') as json_file:
    idpass = json.load(json_file)
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
    time.sleep(5)
    email = browser.find_element_by_xpath("//*[@id='identifierId']")
    time.sleep(2)
    #Entering Email ID
    email.send_keys(idpass['email'], Keys.ENTER)
    time.sleep(5)
    password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    time.sleep(5)
    #Entering Password
    password.send_keys(idpass['password'], Keys.ENTER)
    time.sleep(5)
    #Opening the meet link
    browser.get(sub)
    time.sleep(10)
    #Turning off video
    browser.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
    time.sleep(5)
    # turning off audio
    browser.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()
    time.sleep(30)
    # Join class
    browser.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]").click()
