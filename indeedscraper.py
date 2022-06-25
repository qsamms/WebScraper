from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

print("Please only enter 1 space between words")
jobsearch = input("What kind of jobs are you looking for?")
stripped = jobsearch.strip()
fixedjob = stripped.replace(" ","%20")
location = input("What location?")
stripped = location.strip()
fixedlocation = stripped.replace(" ","%20")
print("Enter your qualifications, and keywords you would like to see in a workplace")
print("To help better match you with a company, type 'done' when done")

stop = False
keywords = []
fixedwords = []
while not stop:
    temp = input()
    if(temp == 'done'):
        break
    keywords.append(temp)
    
for word in keywords:
    one = str(word).strip()
    two = one.replace(" ","")
    newword = two.lower()
    fixedwords.append(newword)

print(fixedwords)

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
    print(f"Compant rating: {correctrating}")

    button = WebDriverWait(driver,30).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,"iframe")))
    try:
        linkcontainer = driver.find_element(By.XPATH,'//div[@id="viewJobButtonLinkContainer"]')
        link = linkcontainer.find_element(By.TAG_NAME,'a')
        linkdisplay = link.get_attribute("href")
    except nosuchelementexcpetion:
        
    description = driver.find_element(By.XPATH,'//div[@class="jobsearch-jobDescriptionText"]').text
    driver.switch_to.parent_frame()

    if(i != len(infos) - 1):
        element2 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((titles[i+1])))
        titles[i+1].click()

    wholething = titles[i].text + justname + location + correctrating + description

    wholethingstripped = str(wholething).strip()
    wholethingwithoutspaces = wholethingstripped.replace(" ","")
    fixedwhole = wholethingwithoutspaces.lower()

    print('Your Skills/Needs that match with this Company:')
    for word in fixedwords:
        if word in fixedwhole:
            print(word + " ")
    print(f"Apply here: {linkdisplay}")
    print('\n\n')

time.sleep(10000000)
driver.quit()
quit()


