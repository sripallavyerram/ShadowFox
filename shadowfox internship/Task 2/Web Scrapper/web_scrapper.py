                                # WEB SCRAPPER TASK IN INTERMEDIATE LEVEL
#-------------------------------------------------------------------------------------------------------------------#


import requests                     # Importing Requests Module
from bs4 import BeautifulSoup       # Inporting Beautifulsoup Module

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
url = requests.get("https://www.shadowfox.in/", headers=headers)
                                  # Displaying all the content of url variable

web = BeautifulSoup(url.content,"html.parser")          # Parsing the raw data using html.parser

print(web.prettify())               # Displaying the formatted data usinng prettify function

# Displaying Website Title
print(web.title)

# Displaying Website Title Name
print(web.title.name)

# Displaying Website Title String
print(web.title.string)

# Displaying Website Link or Anchor Tag
print(web.a)

# Displaying Website First Para tag
print(web.p)

# Displaying Website First Heading Tag
print(web.h1)

# Finding Website First Anchor tag
print(web.find("a"))

# Finding Website All H1 or Heading Tag
print(web.find_all("h1"))

# Finding Website Data Using id attribute 
print(web.find(id= "nav-bar"))