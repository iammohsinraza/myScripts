
import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#----------------------------------------------#
#initialization
error = 0
quotes = []
username = ''
password = ''
pageUrl = ''
imageNames = []
info = open('config.txt','r')
driver = ''
#-----getting configuration-----#


mainDirectory = os.getcwd()
def getDriver(driver):
    os.chdir('driver')
    driver = os.listdir()
    driver = driver[0]
    driver = os.getcwd()+'/'+driver
    driver = driver.replace('\\','/')
    os.chdir(mainDirectory)
    return driver
    
def getImageNames(imageNames):
    os.chdir('images')
    imageNames = os.listdir()
    os.chdir(mainDirectory)
    return imageNames
    
def getUserName(uname):
    info = open('config.txt','r')
    data = info.readlines()
    uname = data[0].rstrip()
    info.close()
    return uname
def getPass(passwrd):
    info = open('config.txt','r')
    password = info.readlines()
    passwrd = password[1].rstrip()
    info.close()
    return passwrd
def getUrl(uname):
    info = open('config.txt','r')
    url = info.readlines()
    uname = url[2].rstrip()
    info.close()
    return uname
def getQuotes():
    newQuotes = []
    info = open('status.txt','r')
    quotes = info.readlines()
    for quote in quotes:
        quote = quote.replace('*$$*','')
        newQuotes.append(quote)
    return newQuotes
### Browser Object
quotes = getQuotes()
imageNames = getImageNames(imageNames)
browser = webdriver.Chrome(getDriver(driver))
browser.maximize_window()
browser.implicitly_wait(20)
browser.get("https://m.facebook.com/")

browser.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(getUserName(username))
browser.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(getPass(password))
time.sleep(2)
browser.find_element_by_xpath('//*[@id="u_0_5"]').click()
time.sleep(3)
if browser.current_url =='https://m.facebook.com/login/save-device/?login_source=login#_=_':
    browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/a').click()
time.sleep(2)

browser.get(getUrl(pageUrl))

for session in range(1,len(getImageNames(imageNames))):
    print(session)
    print(mainDirectory+"\n"+os.getcwd())
    browser.execute_script("window.scrollTo(500, document.body.scrollHeight);")
    time.sleep(4)
    browser.find_element_by_xpath('//*[@id="action_bar"]/div[1]/a').click()
    time.sleep(2)
    browser.find_element_by_id('u_0_1j').send_keys(quotes[session])
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="structured_composer_form"]/div[5]/div/div[1]/button[1]').click()
    time.sleep(3)
    pyautogui.typewrite(mainDirectory+"\\images\\"+imageNames[session])
    pyautogui.press('enter')
    time.sleep(8)
    browser.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div[1]/div[3]/div/button[1]').click()
    time.sleep(4)
    browser.get(getUrl(pageUrl))
    time.sleep(4)
##
##
##
##error = 0;
##cwd = os.getcwd()
##listOfFiles = os.listdir(cwd)
##
##
##

##
##print(imagesName)
##
##
#### Images Rename Optional
####for i,image in enumerate(imagesName):
####    i+=1
####    extension = image.split('.',2)
####    extensionIndex = len(extension)
####    extension = '.'+extension[extensionIndex-1]
####    if extension == '.jpg' or extension == '.png' or extension == '.jpeg':
####        if image != str(i)+extension:
####            os.rename(image,str(i)+extension)
##                
##        
##
##
##
##
##os.chdir(cwd)
##print(cwd)
##for image in imagesName:
##    print(image)
