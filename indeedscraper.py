from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

print("Please only enter 1 space between words")
jobsearch = input("What kind of jobs are you looking for?")
stripped = jobsearch.strip()
fixedjob = stripped.replace(" ","%20")
location = input("What location?")
stripped = location.strip()
fixedlocation = stripped.replace(" ","%20")

driver = webdriver.Chrome()
indeedURL = "https://www.indeed.com/jobs?q="+fixedjob+"&l="+fixedlocation
driver.get(indeedURL)
print(indeedURL)

Jobs = driver.find_elements(By.XPATH,'//div[@class="job_seen_beacon"]')

titles = []
for job in Jobs:
    titles.append(job.find_element(By.TAG_NAME,'a'))

infos = driver.find_elements(By.XPATH,'//div[@class="heading6 company_location tapItem-gutter companyInfo"]')

for i in range(len(infos)):
    print(titles[i].text)
    print(infos[i].text)
    print()

driver.quit()
quit()


