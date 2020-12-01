#crawling comment of ramen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyautogui

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = options, executable_path = "/Users/chihsintseng/Downloads/chromedriver")
link = 'https://www.google.com/maps/d/u/0/viewer?fbclid=IwAR3O8PKxMuqtqb2wMKoHKe4cCETwnT2RSCZSpsyPPkFsJ6NpstcrDcjhO2k&mid=1I8nWhKMX1j8I2bUkN4qN3-FSyFCCsCh7&ll=24.807740000000006%2C120.96740199999999&z=8'
driver.get(link)
time.sleep(1)

#關掉三個月內開幕的選項
first_cl = driver.find_element_by_xpath("//div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[3]")
first_cl.click()

#把台北基隆剩下的打開爬下台北基隆評論
start_search_btn = driver.find_element_by_xpath("//div[170]/span")
start_search_btn.click()
store_name = []
for items in range(167):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[2]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後上滑關掉台北的選項並打開新北選項
pyautogui.scroll(20, x = 250, y = 500)
time.sleep(0.5)
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div[3]").click()
start_search_btn1 = driver.find_element_by_xpath("//div[50]/span")
start_search_btn1.click()

for items in range(47):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[3]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後上滑關掉新北的選項並打開桃竹苗選項
pyautogui.scroll(20, x = 250, y = 500)
time.sleep(0.5)
driver.find_element_by_xpath("//div[3]/div/div/div[3]").click()
start_search_btn2 = driver.find_element_by_xpath("//div[62]/span")
start_search_btn2.click()

for items in range(59):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[4]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後上滑關掉桃竹苗的選項並打開中彰投選項
pyautogui.scroll(20, x = 250, y = 500)
time.sleep(0.5)
driver.find_element_by_xpath("//div[2]/div[4]/div/div/div[3]").click()
pyautogui.scroll(-5, x = 250, y = 500)
start_search_btn3 = driver.find_element_by_xpath("//div[71]/span")
start_search_btn3.click()

for items in range(68):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[5]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後上滑關掉中彰投的選項並打開雲嘉南選項
pyautogui.scroll(20, x = 250, y = 500)
time.sleep(0.5)
driver.find_element_by_xpath("//div[5]/div/div/div[3]").click()
pyautogui.scroll(-5, x = 250, y = 500)
start_search_btn4 = driver.find_element_by_xpath("//div[6]/div/div[3]/div[40]/span")
start_search_btn4.click()

for items in range(37):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[6]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後上滑關掉雲嘉南的選項並打開高屏選項
pyautogui.scroll(20, x = 250, y = 500)
time.sleep(0.5)
driver.find_element_by_xpath("//div[6]/div/div/div[3]").click()
pyautogui.scroll(-5, x = 250, y = 500)
start_search_btn5 = driver.find_element_by_xpath("//div[53]/span")
start_search_btn5.click()

for items in range(50):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[7]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後上滑關掉高屏的選項並打開宜花東選項
pyautogui.scroll(20, x = 250, y = 500)
time.sleep(0.5)
driver.find_element_by_xpath("//div[7]/div/div/div[3]").click()
pyautogui.scroll(-5, x = 250, y = 500)
start_search_btn6 = driver.find_element_by_xpath("//div[15]/span")
start_search_btn6.click()

for items in range(12):
    num = str(items + 3)
    driver.find_element_by_xpath("//div[8]/div/div[3]/div["+ num +"]/div[2]/div").click()
    time.sleep(1)
    s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
    print(s1[0].text)
    s = s1[1].text.split("\n")
    a = list(filter(None, s))
    store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
    store_name.append(s1[0].text)
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
    time.sleep(1)
#爬完之後關掉宜花東的選項並爬離島選項
time.sleep(0.5)
driver.find_element_by_xpath("//div[8]/div/div/div[3]").click()

driver.find_element_by_xpath("//div[3]/div[2]/div[2]/div").click()
time.sleep(1)
s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print(s1[0].text)
s = s1[1].text.split("\n")
a = list(filter(None, s))
store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
store_name.append(s1[0].text)
time.sleep(0.5)
driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(1)

driver.find_element_by_xpath("//div[9]/div/div[3]/div[3]/div[2]/div").click()
time.sleep(1)
s1 = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="qqvbed-p83tee-lTBxed"]')))
print(s1[0].text)
s = s1[1].text.split("\n")
a = list(filter(None, s))
store_char = []
    for i in range(len(a)):
        if "▎特色：" == a[i]:
            start = i
        if "▎營業時間：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_char.append(a[start+k+1])
    ans = "".join(store_char)
    print(ans)
    
    store_time = []
    for i in range(len(a)):
        if "▎營業時間：" == a[i]:
            start = i
        if "▎鄰近地標或大眾運輸：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_time.append(a[start+k+1])
    ans = "".join(store_time)
    print(ans)
    
    store_tran = []
    for i in range(len(a)):
        if "▎鄰近地標或大眾運輸：" == a[i]:
            start = i
        if "▎社團內參考食記：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_tran.append(a[start+k+1])
    ans = "".join(store_tran)
    print(ans)
    
    store_refs = []
    for i in range(len(a)):
        if "▎社團內參考食記：" == a[i]:
            start = i
        if "▎標籤：" == a[i]:
            end = i
    l = int(end - start)-1
    for k in range(l):
        store_refs.append(a[start+k+1])
    ans = "".join(store_refs)
    print(ans)
    
    store_tags = []
    for i in range(len(a)):
        if "▎標籤：" == a[i]:
            start = i
        if a[-1] == a[i]:
            end = i
    l = int(end - start)
    for k in range(l):
        store_tags.append(a[start+k+1])
    ans = "".join(store_tags)
    print(ans)
store_name.append(s1[0].text)
time.sleep(0.5)
driver.find_element_by_xpath("//div[3]/div/div/span/span/span").click()
time.sleep(1)
