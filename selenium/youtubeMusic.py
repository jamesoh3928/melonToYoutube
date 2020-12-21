import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get("https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=481753852&memberKey=45064906&ref=copyurl&snsGate=Y")
time.sleep(1)
songs = []
artists = []
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
passw = open('password.txt',"r",encoding="utf-8")   
password = passw.readline()
passw.close()
user = open('username.txt',"r",encoding="utf-8")   
username = user.readline()
user.close()
print("username: ", username)

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
time.sleep(1)

driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
# driver.find_element_by_xpath('<div class="BHzsHc">다른 계정 사용</div>')
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

# driver.get("https://www.google.com/")

# email = driver.find_element_by_css_selector("#identifierId")
# email.send_keys(username)
# nextB = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
# time.sleep(3)
# passwordBar = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
# passwordBar.send_keys(password)
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
# time.sleep(2)

# 2. Create the playlist
# driver.get("https://music.youtube.com/")
# driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]/iron-icon").click()
# searchBar = driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input")
# for title in songs:
#     searchBar.send_keys(title)
#     searchBar.send_keys(Keys.RETURN)
#     driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/ytmusic-menu-renderer/paper-icon-button/iron-icon")
#     time.sleep(1)
#     driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-popup-container/iron-dropdown/div/ytmusic-menu-popup-renderer/paper-listbox/ytmusic-menu-service-item-renderer[2]").click()
# TODO TEST IT, Make it more structured!!!!


time.sleep(10)

driver.quit()