from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyautogui
import time

options = webdriver.ChromeOptions()
#options.add_argument("headless") #無新視窗

driver = webdriver.Chrome(options = options, executable_path = "/Users/chihsintseng/Downloads/chromedriver")
#driver.maximize_window()
link = 'https://www.google.com/maps/d/u/0/viewer?fbclid=IwAR3O8PKxMuqtqb2wMKoHKe4cCETwnT2RSCZSpsyPPkFsJ6NpstcrDcjhO2k&mid=1I8nWhKMX1j8I2bUkN4qN3-FSyFCCsCh7&ll=24.807740000000006%2C120.96740199999999&z=8'
driver.get(link)
time.sleep(5)

#關掉三個月內開幕的選項
first_cl = driver.find_element_by_xpath("//div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]")
first_cl.click()

#關掉不用的選單（台北基隆、新北、桃竹苗）
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div[3]").click()
driver.find_element_by_xpath("//div[3]/div/div/div[3]").click()
driver.find_element_by_xpath("//div[2]/div[4]/div/div/div[3]").click()
driver.find_element_by_xpath("//div[5]/div/div/div[3]").click()
driver.find_element_by_xpath("//div[6]/div/div/div[3]").click()

#要下滑
pyautogui.scroll(-10)

#關掉不用的選單（宜花東、離島、台灣之外）
#driver.find_element_by_xpath("//div[8]/div/div/div[3]").click()
#driver.find_element_by_xpath("//div[9]/div/div/div[3]").click()
#driver.find_element_by_xpath("//div[10]/div/div/div[3]").click()

#把高雄屏東剩下項目打開
start_search_btn = driver.find_element_by_xpath("//div[@id='legendPanel']/div/div/div[2]/div/div/div[2]/div[7]/div/div[3]/div[53]/span")
start_search_btn.click()
#打開高雄屏東第一間評論（要關）
driver.find_element_by_xpath("//div[7]/div/div[3]/div[3]/div[2]/div").click()
time.sleep(3)
s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print([i.text for i in s1])

driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(3)

#打開高雄第二間評論（要關）
driver.find_element_by_xpath("//div[7]/div/div[3]/div[4]/div[2]/div").click()
time.sleep(3)

s2 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print([j.text for j in s2])

driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(3)

#打開高雄第三間評論（要關）
driver.find_element_by_xpath("//div[7]/div/div[3]/div[5]/div[2]/div").click()
time.sleep(3)

s3 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print([k.text for k in s3])

driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(3)

#store = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="suEOdc"]')))
#print([i.text for i in store])

#driver.close()
