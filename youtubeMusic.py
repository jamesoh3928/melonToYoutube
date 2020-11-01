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
# 1. Login part to Youtube Music (do not actually login)
# 2. Create the playlist
# 3. structure the searching part

#Youtube Music
# driver.get("https://music.youtube.com/")
# search = driver.find_element_by_xpath("/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/span")
# search.click()
time.sleep(1)

driver.quit()