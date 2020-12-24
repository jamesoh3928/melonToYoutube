import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--incognito")

def hover(self):
    wd = webdriver_connection.connection
    element = wd.find_element_by_link_text(self.locator)
    hov = ActionChains(wd).move_to_element(element)
    hov.perform()

driver = webdriver.Chrome(options=options)
driver.get("https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=481753852&memberKey=45064906&ref=copyurl&snsGate=Y")
songs = []
artists = []
nextXpath = '/html/body/div/div[2]/div/div/div[2]/div/div[2]/div/span/a['
numOfSongs = 0
numOfButtons = 0
delay = 10

try:
    numSongsElem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div/h3/span"))
    )
    numOfSongs = int(numSongsElem.text[1:-1])
    numOfButtons = numOfSongs // 50 + 1
except Exception as e:
    print(e)

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
        continue
    
#Checking if data were crawled
print(len(songs), len(artists))
for i in range(len(songs)):
    print(songs[i], "     ", artists[i])

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

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="openid-buttons"]/button[1]'))
    ).click()
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    ).send_keys(username)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/div[2]'))
    ).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))
    ).send_keys(password)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))
    ).click()

except Exception as e:
    print(e)

# 2. Create the playlist
time.sleep(3)
driver.get("https://music.youtube.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]/iron-icon'))
).click()

searchBar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input'))
)

# 3. Add to playlist
for i in range(len(songs)):
    searchBar.clear()
    searchBar.send_keys(songs[i] + " " + artists[i] + " " + "노래")
    searchBar.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="contents"]/ytmusic-responsive-list-item-renderer/div[2]'))
        hover.perform()
        print("Hello")
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/ytmusic-menu-renderer/paper-icon-button/iron-icon'))).click()
        time.sleep(1)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="items"]/ytmusic-menu-navigation-item-renderer[2]'))).click()
        time.sleep(1)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="playlists"]/ytmusic-playlist-add-to-option-renderer/button'))).click()
        time.sleep(1)
    except Exception as e:
        print(e)
        continue

# TODO TEST IT, Make it more structured!!!! (Use Action Chain?)

driver.quit()