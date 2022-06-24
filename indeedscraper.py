from urllib import response
import requests
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import urllib3

print("Please only enter 1 space between words")
jobsearch = input("What kind of jobs are you looking for?")
stripped = jobsearch.strip()
fixedjob = stripped.replace(" ","%20")
location = input("What location?")
stripped = location.strip()
fixedlocation = stripped.replace(" ","%20")

s = requests.Session()
indeedURL = "https://www.indeed.com/jobs?q="+fixedjob+"&l="+fixedlocation
print(indeedURL)
indeedPage = s.get(indeedURL)
indeedSoup = BeautifulSoup(indeedPage.content,"html.parser")

indeedJobs = indeedSoup.find_all("div", class_ = "job_seen_beacon")


for job in indeedJobs:
    companyTitleInfo = job.find("a", class_ = "jcs-JobTitle")
    jobTitle = companyTitleInfo.find("span")
    companyInfo = job.find("div", class_ = "heading6 company_location tapItem-gutter companyInfo")
    companyname = companyInfo.find("a", class_ = "turnstileLink companyOverviewLink")
    if companyname == None:
        companyname = companyInfo.find("span", class_ = "companyName")
    location = companyInfo.find("div", class_ = "companyLocation")

    print(f"Job Title: {jobTitle.text}")
    print(f"Company: {companyname.text}")
    print(f"Location: {location.text}")
    print()
    
