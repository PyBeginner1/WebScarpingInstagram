from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os
import wget
import time

#connect webdriver to this notebook
driver = webdriver.Chrome('D:/TestPython/venv/Scripts/chromedriver.exe')    #WebDriver is an open source tool for automated testing of webapps across many browsers.
#post the url you want to scrap
driver.get("http://www.instagram.com")


#we need to target input fields i.e., username & password
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))

#clear the username & password fields
username.clear()
password.clear()

#typing values into the fields
username.send_keys("shashvathn")                    #type your username
password.send_keys("Legend")                        #type password, its fake

#for clicking submit
login=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()

not_now=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))).click()
not_now2=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()


#for search field in instagram after logging in
#searchbox=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Search']")))
#clear the search field
#searchbox.clear()
#input something into search field
#searchbox.send_keys("kimk")

#above can be done using xpath
#for search field in instagram after logging in
searchbox=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
#clear the search field
searchbox.clear()
#input something into search field
keyword='#dogs'
searchbox.send_keys(keyword)
#to hit enter
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

#scroll
driver.execute_script("window.scrollTo(0,4000);")           #window.scrollTo(xpos, ypos) in pixels
images = driver.find_elements_by_tag_name('img')
images =[image.get_attribute('src') for image in images]
images

#creating a folder
path=os.getcwd()
path=os.path.join(path, keyword[1:] + 's')                  #keyword[1:]= #cat to cat
os.mkdir(path)
path

#save images into folder
counter=0
for image in images:
    save_as=os.path.join(path,keyword[1:] + str(counter) + '.jpg')
    wget.download(image,save_as)
    counter +=1
