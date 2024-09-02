from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver_path = os.path.join(os.getcwd(),'chromedriver-win64')
print(driver_path)

exe_path = os.path.join(driver_path,'chromedriver.exe')
print(exe_path)

driver = webdriver.Chrome()

driver.maximize_window()

# destination = driver.get()
driver.get('https://www.rokomari.com/search?term=programming+books&xyz=&search_type=ALL&publisherIds=4815&priceRange=0to114900&discountRange=0to30')

link_list = []
num_pages = 2
for page in range(1, num_pages + 1):
    # Construct URL for each page
    url = f'https://www.rokomari.com/search?term=programming+books&xyz=&search_type=ALL&publisherIds=4815&priceRange=0to114900&discountRange=0to30?page={page}'
    driver.get(url)
    time.sleep(2)
    for i in range(1, 61):
        j = str(i)
        link = driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/section[2]/div[2]/div/div[1]/div/div/a['+j+']/html/body/div[7]/div/div/div/section[2]/div[2]/div/div[1]/div/a/div[1]/img').get_attribute('href')
    
        link_list.append(link)

print(link_list)
total_items_scraped = len(link_list)
print(f"Total number of items scraped: {total_items_scraped}")
