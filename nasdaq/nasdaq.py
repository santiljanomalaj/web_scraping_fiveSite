from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
import random

# define & generate the title of the earning-dtail_number.csv
f_earning_num = open('./earnings-detail_number-of-estimates-changed.csv','w')
f_earning_num.write('symbol_id,universal_site_symbol,site_symbol,timestamp,estimate_changed,number_of_estimates_changed,summary')

# define & generate the title of the earning_quarterly.csv
f_earning_quarterly = open('./earnings-detail_quarterly-earnings-forecast.csv','w')
f_earning_quarterly.write('symbol_id,universal_site_symbol,site_symbol,timestamp,fiscal_year_end,consensus_eps*_forecast,high_eps*_forecast,low_eps*_forecast,number_of_estimates,over_the_last_4_weeks_number_of_revisions_-_up,over_the_last_4_weeks_number_of_revisions_-_down')

# define & generate the title of the earning_quarterly.csv
f_earning_yearly = open('./earnings-detail_yearly-earnings-forecast.csv','w')
f_earning_yearly.write('symbol_id,universal_site_symbol,site_symbol,timestamp,fiscal_year_end,consensus_eps*_forecast,high_eps*_forecast,low_eps*_forecast,number_of_estimates,over_the_last_4_weeks_number_of_revisions_-_up,over_the_last_4_weeks_number_of_revisions_-_down')

# retrieve proxy IP addresses from best-private-proxies.txt file
proxies = open("best-private-proxies.txt", "rt")
proxy = proxies.read()         
proxies.close()                   
proxy_list = proxy.split("\n")

def earning_details():
  
  flag=0
  # get proxy_ip
  random_index = random.randint(0, len(proxy_list))
  proxy_ip=get_proxies(random_index)

  # set proxy & option
  options = Options()
  options.add_argument("--prox-server=%s" % proxy_ip)
  options.add_argument("--window-size=1466,868")
  options.add_argument("--disable-notifications")
  options.add_argument("--lang=en")

  # run chromdriver
  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

  driver.get('https://www.nasdaq.com/market-activity/stocks/aapl/earnings')

  time.sleep(5)
  earning_detail=driver.page_source
  earnings=soup(earning_detail, 'html.parser')

  # get Number of Estimates Changed
  number_of_estimates=earnings.findAll('tr',{'class','estimate-momentum__row estimate-momentum__row--body'})
  
  symbol_id='342'
  universal_site_symbol='US_XNAS_AAPL'
  site_symbol=earnings.find('span', {'class','symbol-page-header__symbol'}).text
  summary=earnings.find('p',{'class','estimate-momentum__section estimate-momentum__info'}).text
  now = datetime.now()
  timestamp= now.strftime("%Y-%m-%d-%H-%M")

  for number_estimate in number_of_estimates:
    estimate_changed=number_estimate.th.text
    number_estimates_changed=number_estimate.td.text
    if flag==0:
      print(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+estimate_changed+','+number_estimates_changed+','+summary)
      f_earning_num.write('\n')
      f_earning_num.write(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+estimate_changed+','+number_estimates_changed+','+summary)
      flag=1
    f_earning_num.write('\n')
    print(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+estimate_changed+','+number_estimates_changed)
    f_earning_num.write(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+estimate_changed+','+number_estimates_changed)
      
  # get detail_quarterly
  quarterly_forecast=earnings.findAll('tr',{'class','earnings-forecast__row earnings-forecast__row--body'})
  for quarterly in quarterly_forecast:
    fiscal_year_end=quarterly.th.text
    quarterly_td=quarterly.findAll('td')
    consensus_eps=quarterly_td[0].text
    high_eps=quarterly_td[1].text
    low_eps=quarterly_td[2].text
    number_of_estimate=quarterly_td[3].text
    number_revision_up=quarterly_td[4].text
    number_revision_down=quarterly_td[5].text
    print(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+fiscal_year_end+','+consensus_eps+','+high_eps+','+high_eps+','+low_eps+','+number_of_estimate+','+number_revision_up+','+number_revision_down)
    f_earning_quarterly.write('\n')
    f_earning_quarterly.write(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+fiscal_year_end+','+consensus_eps+','+high_eps+','+high_eps+','+low_eps+','+number_of_estimate+','+number_revision_up+','+number_revision_down)
  
  # get yearly earnings forcast
  yearly_earnings=earnings.findAll('tr',{'class':'earnings-forecast__row earnings-forecast__row--body'})
  for yearly in yearly_earnings:
    yearly_fiscal_year_end=yearly.th.text
    yearly_td=yearly.findAll('td')
    yearly_consensus_eps=yearly_td[0].text
    yearly_high_eps=yearly_td[1].text
    yearly_low_eps=yearly_td[2].text
    yearly_number_of_estimate=yearly_td[3].text
    yearly_number_revision_up=yearly_td[4].text
    yearly_number_revision_down=yearly_td[5].text
    print(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+yearly_fiscal_year_end+','+yearly_consensus_eps+','+yearly_high_eps+','+yearly_low_eps+','+yearly_number_of_estimate+','+yearly_number_revision_up+','+yearly_number_revision_down)
    f_earning_yearly.write('\n')
    f_earning_yearly.write(symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+yearly_fiscal_year_end+','+yearly_consensus_eps+','+yearly_high_eps+','+yearly_low_eps+','+yearly_number_of_estimate+','+yearly_number_revision_up+','+yearly_number_revision_down)
def revenue_eps():
  flag=0
  # get proxy_ip
  random_index = random.randint(0, len(proxy_list)-1)
  proxy_ip=get_proxies(random_index)

  # set proxy & option
  options = Options()
  options.add_argument("--prox-server=%s" % proxy_ip)
  options.add_argument("--window-size=1466,868")
  options.add_argument("--disable-notifications")
  options.add_argument("--lang=en")

  # run chromdriver
  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

  driver.get('https://www.nasdaq.com/market-activity/stocks/coke/revenue-eps')

  time.sleep(10)
  revenue_detail=driver.page_source
  revenues=soup(revenue_detail, 'html.parser')

  symbol_id='342'
  universal_site_symbol='US_XNAS_AAPL'
  site_symbol=revenues.find('span', {'class','symbol-page-header__symbol'}).text
  now = datetime.now()
  timestamp= now.strftime("%Y-%m-%d-%H-%M")

  # get revenues
  year_revenues=revenues.findAll('th',{'class':'revenue-eps__table-heading'})
  revenue_print=''
  for year_revenue in year_revenues:
    revenue_eps_row=revenues.findAll('tr',{'class':'revenue-eps__row'})
    revenue_year=''
    revenue_item=[]
    revenue_list=[]
    if flag==0:
      flag=1
      continue
    for x in range(len(revenue_eps_row)):
      if x==0:
        continue
      if x%4==1:
        revenue_year=revenue_eps_row[x].th.text
        continue
      revenue_td=revenue_eps_row[x].findAll('td')
      # revenue=revenue_td[0].text
      # eps=revenue_td[1].text
      # dividends=revenue_td[2].text
      revenue_print=symbol_id+','+universal_site_symbol+','+site_symbol+','+timestamp+','+year_revenue.text+','+revenue_year
      revenue_list=[]
      for y in range(len(revenue_td)):
        revenue_list.append(revenue_td[y].text)
      revenue_item.append(revenue_list)

    for a in range(len(revenue_eps_row)-6):
      revenue_result=''
      for b in range(len(revenue_eps_row[a].findAll('td'))):
        revenue_result+=revenue_print+revenue_item[b][a]
      print(revenue_result)

      # for y in range(len(revenue_td)-1):
      #   revenue_print+=revenue_td[y].text
      # print(revenue_print)
      
def get_proxies(index): 
  return proxy_list[index]

# earning_details()
revenue_eps()