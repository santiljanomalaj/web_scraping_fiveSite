from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
import random

# define the tille in the earning-detail.csv file

f = open('./fidelity/key-sttistics.csv','w',encoding='utf-8')
f.write('category,ratio,company,industry,industry_percentile')

# chrome option settings
options = Options()
options.add_argument("--window-size=1466,868")
options.add_argument("--disable-notifications")
options.add_argument("--lang=en")

# run chromedriver

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://snapshot.fidelity.com/fidresearch/snapshot/landing.jhtml#/keyStatistics?symbol=AAPL")

time.sleep(5)
try:
  driver.find_element_by_xpath('//*[@id="alreadyMember"]/p[2]/a').click()
except NoSuchElementException:
  pass

#login part
Access_id="123qwe123qwe"
password="123234345"
time.sleep(1)
driver.find_element_by_xpath('//*[@id="member-id-field"]').send_keys(Access_id)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password-field"]').send_keys(password)
time.sleep(random.randint(2,5))
driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/form/div/table/tbody/tr[5]/td/a').click()

# get a key_statictics
driver.get("https://snapshot.fidelity.com/fidresearch/snapshot/landing.jhtml#/keyStatistics?symbol=AAPL")
time.sleep(4)
key_statictics_page=driver.page_source
key_statictics=soup(key_statictics_page, 'html.parser')

flag=0
headers="headers"
company=key_statictics.find('th',{'class':'top-bottom-border lft-rt-border right'}).text
ratio=key_statictics.find('th',{'class':'top-bottom-border'}).text
industry=key_statictics.find('th',{'class':'top-bottom-border rt-border right'}).text
industry_percentile=key_statictics.find('th',{'class':'top-bottom-border right'}).text
f.write('\n')
f.write(headers+','+ratio+','+company+','+industry+','+industry_percentile)

driver.execute_script("window.scrollTo(0, 300);")
time.sleep(2)
driver.execute_script("window.scrollTo(300, 600);")
time.sleep(2)
driver.execute_script("window.scrollTo(600, 900);")
time.sleep(2)
driver.execute_script("window.scrollTo(900, 1200);")

category_names=key_statictics.findAll('div',{'class','header-with-border'})
category_package=key_statictics.findAll('div',{'id':'audit-integrity'})

for category_name in category_names:
  category_nicname=category_name.h3.text
  for category in category_package:
    tr_rows=category.findAll('tr')
    for row in tr_rows:
      if (flag==0):
        continue
        flag=1
      ratio=row.td.text
      company=row.find('td', {'class':'lft-rt-border right'})
      industry=row.find('td',{'class':'rt-border right'})
      industry_percentile=row.find('td',{'class':'right'})
      print(category_nicname+','+ratio+','+company+','+industry+','+industry_percentile)
      f.write(category_nicname+','+ratio+','+company+','+industry+','+industry_percentile)
      flag=0



