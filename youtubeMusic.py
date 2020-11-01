import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get("https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=481753852&memberKey=45064906&ref=copyurl&snsGate=Y")
time.sleep(3)
songs = []
artists = []
print(driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div/div[2]/div/span/a[1]'))
nextXpath = '/html/body/div/div[2]/div/div/div[2]/div/div[2]/div/span/a['
numOfSongs = int(driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/h3/span").text[1:-1])
numOfButtons = numOfSongs // 50 + 1
for i in range(numOfButtons):
    try: 
        songObj = driver.find_elements_by_css_selector(".fc_gray")
        for obj in songObj:
            songs.append(obj.text)

        artistObj = driver.find_elements_by_css_selector("#artistName")
        for obj in artistObj:
            artists.append(obj.text)
        driver.find_element_by_xpath(nextXpath + str(i + 1) + "]").click()
        time.sleep(1)
    except Exception as e:
        print(e)
    
#Checking if data were crawled
print(songs)
print(artists)
print(len(songs), len(artists))
#TODO 
# 1. Login part to Youtube Music (do not actually login) - search python selenium secured login in youtube
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fpremium&hl=ko&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(3)

passw=open('password.txt',"r",encoding="utf-8")   
password=str(passw.read())
user=open('username.txt',"r",encoding="utf-8")   
username=str(user.read())

email = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email.send_keys(username)
nextB = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
time.sleep(3)
passwordBar = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
passwordBar.send_keys(password)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
time.sleep(2)
# 2. Create the playlist
driver.get("https://music.youtube.com/")
driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]/iron-icon").click()
searchBar = driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input")
for title in songs:
    searchBar.send_keys(title)
    searchBar.send_keys(Keys.RETURN)
    driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/ytmusic-menu-renderer/paper-icon-button/iron-icon")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown/div/ytmusic-menu-popup-renderer/paper-listbox/ytmusic-menu-service-item-renderer[2]").click()
# TODO TEST IT, Make it more structured!!!!


time.sleep(1)

driver.quit()