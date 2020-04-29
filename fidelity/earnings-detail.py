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

f = open('./fidelity/earnings-detail.csv','w')
f.write('symbol_id,universal_site_symbol,site_symbol,timestamp,quarter,report_date, report_time, consensus_est._eps_($)_(s), analyst, adjusted_actuals_eps_($), low, high, thomson_reuters_starmine_smartestimate_($)_, company_reported_gaap_eps_($), _reported_eps_($)')

# chrome option settings
options = Options()
options.add_argument("--window-size=1466,868")
options.add_argument("--disable-notifications")
options.add_argument("--lang=en")

# run chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://eresearch.fidelity.com/eresearch/evaluate/fundamentals/earnings.jhtml?tab=details&symbols=AAPL")

try:
  driver.find_element_by_xpath('//*[@id="alreadyMember"]/p[2]/a').click()
except NoSuchElementException:
  pass

#login part
Access_id="123qwe123qwe"
password="123234345"
time.sleep(3)
driver.find_element_by_xpath('//*[@id="member-id-field"]').send_keys(Access_id)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password-field"]').send_keys(password)
time.sleep(random.randint(2,5))
driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/form/div/table/tbody/tr[5]/td/a').click()

# get the earning-detail
time.sleep(1)
driver.find_element_by_xpath('//*[@id="com_fidelity_retail_earningsdetail_history"]/div/div/div/ul/li/a').click()

driver.execute_script("window.scrollTo(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollTo(200, 400);")
time.sleep(2)

earning_page=driver.page_source
earnings_detail=soup(earning_page, 'html.parser')

table_data=earnings_detail.find('table',{'class':'table borderTop'}).find('tbody')
table_data_rows=table_data.findAll('tr')

for row in table_data_rows:
  symbol_id="343"
  universal_site_symbol="US_XNAS_AAPL"
  site_symbol=earnings_detail.find('span',{'id':'headerSymbol'}).text
  now = datetime.now()
  timestamp= now.strftime("%Y-%m-%d-%H-%M")
  quarter=row.th.text
  row_td=row.findAll('td')
  report_date=row_td[0].text
  report_time=row_td[1].text
  consensus_Est=row_td[2].text
  consensus=consensus_Est.split('(')
  consensus_est_eps=consensus[0]
  temp=consensus[1].split(')')
  analyst=temp[0]
  adjusted_actuals_eps=row_td[3].text
  eps_difference=row_td[4].text
  est_Low_High=row_td[5].text
  low_high=est_Low_High.split('/')
  low=low_high[0]
  high=low_high[1]
  thomson_reuters_starmine_smartestimate=row_td[6].text
  gaap_Eps=row_td[7].text
  reported_eps=row_td[8].text
  print(symbol_id+', '+universal_site_symbol+', '+site_symbol+', '+timestamp+', '+quarter+', '+report_date+', '+report_time+', '+consensus_est_eps+', '+analyst+', '+adjusted_actuals_eps+', '+eps_difference+', '+low+', '+high+', '+thomson_reuters_starmine_smartestimate+', '+gaap_Eps+', '+reported_eps)
  f.write('\n')
  f.write(symbol_id+', '+universal_site_symbol+', '+site_symbol+', '+timestamp+', '+quarter+', '+report_date+', '+report_time+', '+consensus_est_eps+', '+analyst+', '+adjusted_actuals_eps+', '+eps_difference+', '+low+', '+high+', '+thomson_reuters_starmine_smartestimate+', '+gaap_Eps+', '+reported_eps)





