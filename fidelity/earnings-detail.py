from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# chrome option settings
options = Options()
options.add_argument("--window-size=1466,868")
options.add_argument("--disable-notifications")
options.add_argument("--lang=en")

# run chromedriver
driver = webdriver.Chrome("E:/working_folder/webs_craping(canada)/chromedriver.exe", ChromeDriverManager().install(), chrome_options=options)