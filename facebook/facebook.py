#import librabries
import time
import pyautogui
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#----------------------------------------------#

#-----getting configuration-----#

config_file = open('config.txt','r')
cwd  =  os.getcwd()
print(cwd)
line = config_file.readlines()

###-----User email address------#
userEmail = line[0].split('>')
userEmail = userEmail[1].rstrip()

###-----User password-----#
userPass = line[1].split('>')
userPass = userPass[1].rstrip()
##
###-----Image folder location-----#
img_fol_loc = "images/"

##
###-----driver folder location-----#
dri_fol_loc = line[3].split('>')
dri_fol_loc = dri_fol_loc[1].rstrip()
###-----Description-----#
desc = line[5].split('>')
desc = desc[1].rstrip()
###-----max pics-----#
max_pic = line[6].split('>')
max_pic = max_pic[1].rstrip()
##------info_file---------------##
info_file = line[4].split('>')
info_file = info_file[1].rstrip()


browser = webdriver.Chrome(dri_fol_loc)


browser.maximize_window()
browser.implicitly_wait(20) 


browser.get("https://m.facebook.com/")

browser.find_element_by_xpath('//*[@id="m_login_email"]').send_keys(userEmail)
browser.find_element_by_xpath('//*[@id="m_login_password"]').send_keys(userPass)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="u_0_5"]').click()
time.sleep(6)
browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/a').click()
time.sleep(1)
browser.get("https://m.facebook.com/bazmerizviaofficial/")
browser.execute_script("window.scrollTo(500, document.body.scrollHeight);")
time.sleep(4)
browser.find_element_by_xpath('//*[@id="action_bar"]/div[1]/a').click()
time.sleep(2)

browser.find_element_by_id('u_0_1l').send_keys("salam")
time.sleep(5)
browser.find_element_by_xpath('//*[@id="structured_composer_form"]/div[5]/div/div[1]/button[1]').click()
time.sleep(3)
pyautogui.typewrite('E:\Marketing and Services Facebook\\1.png')
pyautogui.press('enter')
time.sleep(6)
browser.find_element_by_xpath('//*[@id="composer-main-view-id"]/div[1]/div[1]/div[3]/div/button[1]').click()
##
###--------After Log in Process----------#
##
###-------reading add informations------#
##info_file = open(info_file,'r')
##lines = info_file.readlines()
##
##pic = 1
##
##for line in lines:
##        if pic == int(max_pic):
##                pic = 1
##        attributes = line.split(',')
##
##        if len(attributes)==3:
##                prize = 1500
##                
##        title = attributes[0].rstrip()
##        cat = attributes[1].rstrip()
##        sub_cat = attributes[2].rstrip()
##        if len(attributes) == 4:
##                prize = attributes[3].rstrip()
##                
##                
##        if cat.lower() == 'mobile':
##                mobile = '//*[@id="cat-1411"]'
##                cat = mobile
##
##        ###------------CATAGORYS CHARTS---------------###
##        qmobile='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[1]/a'	
##        samsung='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[2]/a'
##        apple='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[3]/a'	
##        nokia='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[4]/a'	
##        lg='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[5]/a'	
##        huawei='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[6]/a'	
##        sony='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[7]/a'	 
##        sonyericsson='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[8]/a'
##        htc='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[9]/a'	
##        motorola='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[10]/a'	
##        oppo='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[11]/a'	
##        lenovo='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[12]/a'
##        haier='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[13]/a'	
##        rivo='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[14]/a'	 
##        blackberry='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[15]/a'	
##        mobilink='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[16]/a'	
##        voice='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[17]/a'	
##        alcatel='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[18]/a'	
##        xioami='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[19]/a'	
##        infinix='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[20]/a'	
##        calme='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[21]/a'	
##        gright='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[22]/a'
##        gfive='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[23]/a'	
##        club='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[24]/a'	
##        inew='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[25]/a'	 
##        othermobiles='//*[@id="category-1453"]/div[2]/div[2]/div/ul/li[26]/a'
##
##        ##----------Sub catagory Validation------------------###
##        if sub_cat.lower() =="qmobile":
##                sub_cat =qmobile
##        if sub_cat.lower() =="samsung":
##                sub_cat = samsung
##        if sub_cat.lower() =="apple":
##                sub_cat =apple
##        if sub_cat.lower() =="nokia":
##                sub_cat =nokia
##        if sub_cat.lower() =="lg":
##                sub_cat =lg
##        if sub_cat.lower() =="huawei":
##                sub_cat =huawei
##        if sub_cat.lower() =="sony":
##                sub_cat =sony
##        if sub_cat.lower() =="sonyericsson":
##                sub_cat =sonyericsson
##        if sub_cat.lower() =="htc":
##                sub_cat =htc
##        if sub_cat.lower() =="motorola":
##                sub_cat =motorola
##        if sub_cat.lower() =="oppo":
##                sub_cat =oppo
##        if sub_cat.lower() =="lenovo":
##                sub_cat =lenovo
##        if sub_cat.lower() =="haier":
##                sub_cat =haier
##        if sub_cat.lower() =="rivo":
##                sub_cat =rivo
##        if sub_cat.lower() =="blackberry":
##                sub_cat =blackberry
##        if sub_cat.lower() =="mobilinkjazzx":
##                sub_cat =mobilink
##        if sub_cat.lower() =="voice":
##                sub_cat =voice
##        if sub_cat.lower() =="alcatel":
##                sub_cat =alcatel
##        if sub_cat.lower() =="xioami":
##                sub_cat =xioami
##        if sub_cat.lower() =="infinix":
##                sub_cat =infinix
##        if sub_cat.lower() =="calme":
##                sub_cat =calme
##        if sub_cat.lower() =="gright":
##                sub_cat =gright
##        if sub_cat.lower() =="gfive":
##                sub_cat =gfive
##        if sub_cat.lower() =="club":
##                sub_cat =club
##        if sub_cat.lower() =="inew":
##                sub_cat =inew
##        if sub_cat.lower() =="othermobiles":
##                sub_cat = othermobiles
##
##
##        ###-------Status of posting------###
##        status = 'Posting'
##        browser.get("https://www.olx.com.pk/posting/")
##
##        time.sleep(4)
##        try:
##                #--------Click on simple form button--------# 
##                browser.find_element_by_xpath('//*[@id="show-gallery-html"]').click()
##        except:
##                print('not click')
##                
##        time.sleep(2)
##        print(status)
##
##        #--------------Adding title to ad-------#
##        browser.find_element_by_name("data[title]").send_keys(title)
##        time.sleep(1)
##
##        #-----------Click on catagory window----------#
##        browser.find_element_by_xpath('//*[@id="choose-category-ilu"]').click()
##        time.sleep(2)
##
##
##        ###--------Middle catagory defaults--------###
##        middle_mobile = '//*[@id="category-1411"]/div[2]/div[2]/div/ul/li[1]/a'
##
##        #-------------Click on Catagory---------###
##        if cat.lower()=='mobile':
##                middle = middle_mobile
##        
##        browser.find_element_by_xpath(cat).click()
##
##                
##
##        browser.find_element_by_xpath('//*[@id="category-1411"]/div[2]/div[2]/div/ul/li[1]/a').click()
##
##
##        browser.find_element_by_xpath(sub_cat).click()
##
##        time.sleep(2)
##
##        browser.find_element_by_xpath('//*[@id="parameter-div-price"]/div[2]/div/div[1]/p/span/input').send_keys(str(prize))
##
##        time.sleep(2)
##
##        browser.find_element_by_xpath('//*[@id="add-description"]').send_keys(desc)
##        browser.find_element_by_xpath('//*[@id="htmlbutton_1"]/input').clear()
##        browser.find_element_by_xpath('//*[@id="htmlbutton_1"]/input').send_keys(str(img_fol_loc)+str(pic)+'.jpg')
##        pic +=1
##        browser.find_element_by_xpath('//*[@id="save"]').click()
##        time.sleep(2)


