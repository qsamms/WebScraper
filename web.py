import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

jobelements = soup.find_all("div", class_ = "card-content")

#print out all job listing information
for job in jobelements:
    title = job.find("h2", class_ = "title is-5")
    company = job.find("h3", class_ = "subtitle is-6 company")
    location = job.find("p", class_ = "location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()

#searching for something specific 
pythonjobelements = []
pythonjobs = soup.find_all("h2", string = lambda text: "python" in text.lower())
for h2element in pythonjobs:
    pythonjobelements.append(h2element.parent.parent.parent)

for pythonjobelement in pythonjobelements:
    title = pythonjobelement.find("h2", class_ = "title is-5")
    company = pythonjobelement.find("h3", class_ = "subtitle is-6 company")
    location = pythonjobelement.find("p", class_ = "location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()


#get links
for job in jobelements:
    links = job.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
