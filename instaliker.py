#v0.0.1
#beinganukul
#time taken around 6 hour
#date 2020 May 9

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#instagram credentials
insta_id = input("Enter Instagram Username:")
insta_pass = getpass("Enter Instagram Password:")

#website url
URL= 'https://www.instagram.com/'

#webdriver imports using chroem as browser
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

#login 
driver.get(URL)
sleep(3)
user = driver.find_element_by_name('username')
passw = driver.find_element_by_name('password')

#types username and password
user.send_keys(insta_id)
passw.send_keys(insta_pass)
#clicks login button
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
#time given to load instagram
sleep(10)
#this will click not now when instagran throws do you want to recieve notificatioins
driver.find_element_by_xpath('//*[contains(@class, "aOOlW   HoLwm ")]').click()

#here comes the fun part this is to repeat or say like 20 posts in ascending order
post_to_like = range(1,20)
#loop starts
for i in post_to_like:
    xpath = "/html/body/div[1]/section/main/section/div/div[2]/div/article[" #i broke this into 3 parts so it would be easier to read the xpath +=str(i) is to increase article number or say insta post
    xpath += str(i)
    xpath +="]/div[2]/section[1]/span[1]/button" #joined all three of them
    driver.find_element_by_xpath(xpath).click() #clicking in the like button
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,xpath))) # this line is intresting webdriver wait allows to load webpage or say let element appear in ui before clicking otherwise it will throw error
    sleep(2) # sleep is here to make instagram not flag user as bot

#the above for loop loops and does all the work
#this will close the chrome instance 
driver.close()
