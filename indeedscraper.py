from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def reverse(x):
    return x[::-1]

for i in range(len(infos)):
    rating = ""
    numflag = False
    counter = 0

    if(infos[i].text != None):
        nameandrating = infos[i].text.splitlines()[0]
        backwards = reverse(nameandrating)
        for x in backwards:
            if(counter == 3):
                break
            if(x.isdigit()):
                numflag = True
                rating = rating + x
            else:
                if(x == '.' and numflag):
                    rating = rating + x
            counter+=1
    
        correctrating = reverse(rating)
        if(correctrating == ""):
            counter = 0
            length = len(nameandrating) - 3
            justname = ''
            for x in nameandrating:
                if not x.isdigit():
                    justname = justname + x
                elif x.isdigit() and counter < length:
                    justname = justname + x
        else:
            justname = ''.join([i for i in nameandrating if not i.isdigit()])

        if(correctrating != ""):
            justname = justname[:-1]

        location = infos[i].text.splitlines()[1]

    print(titles[i].text)
    print(justname)
    print(location)

    if(correctrating == ""):
        correctrating = "N/A"
    print("Company rating: " + correctrating)
    print()

    time.sleep(2)
    iframe = driver.find_element(By.TAG_NAME,"iframe")
    driver.switch_to.frame(iframe)
    description = driver.find_element(By.XPATH,'//div[@class="jobsearch-jobDescriptionText"]').text
    print(description)
    driver.switch_to.parent_frame()
    if(i == len(infos) - 1):
        quit()
    time.sleep(2)
    titles[i+1].click()
    time.sleep(2)
    print()

time.sleep(10000000)
driver.quit()
quit()


