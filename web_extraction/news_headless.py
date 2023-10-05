from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys


application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

website = "https://www.thesun.co.uk/sport/football/"
path = "/home/{name}/Desktop/chromedriver"

# headless
options = Options()
options.headless = True


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# //div[@class="teaser__copy-container"]

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]') 

tittles = []
subtittles = []
links = []

for container in containers:
    tittle = container.find_element(by="xpath", value='/a/span').text
    subtittle = container.find_element(by="xpath", value='/a/h3').text    
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    
    tittles.append(tittle)
    subtittles.append(subtittle)
    links.append(link)
    

my_dict = {'tittle':tittles, 'subtittle':subtittles, 'link':links}
df_headline = pd.DataFrame(my_dict)

file_name = f'{application_path}/headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headline.to_csv(final_path)

driver.quit()