#The idea of this mini project is to create a dataset from Wikipedia
#I have divided this project into different tasks 

#Task 1 Scrape a single movie from the main page and put it in a Python dictionary

from bs4 import BeautifulSoup as bs
import requests
#Load the page

r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3")

soup = bs(r.content, features="lxml")
print(soup.prettify()) Checking that it is working

#Look for the specific information that we want from the webpage
#Grab the table with all the necessary information and scrape from there

info_box = soup.find(class_ = "infobox vevent")

#All our information is under "tr" section
th = key and tr = value for our dictionary
info_rows = info_box.find_all("tr")
for row in info_rows:
    print(row.prettify())

#Let's build the dictionary for this particular movie

def get_content_value(row_data):
    if row_data.find("li"):
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all('li')]
    else:
        return row_data.get_text(" ", strip=True).replace("\xa0", " ")

movie_info = {}

for index, row in enumerate(info_rows):
    if index == 0:
        movie_info["title"] = row.find('th').get_text(" ", strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find("th").get_text(" ", strip=True)
        content_value = get_content_value(row.find("td"))
        movie_info[content_key] = content_value

#Inside some categories there are some list that need to be handled differently
#Create a function that deals with information inside a list
#The function was moved to line 28 after realizing I needed to handled lists differently

#Did some minor clean ups after the fuction in the dictionary created
### .replace("\xa0", " ")
### get.text(" ", strip=True) ### Trimming blank spaces and separating strings that were together

#Task 1 Completed. 

###Task 2: Scrape info box for all movies in the original website
#Go to every link in https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films and collect the data
#from the info box as performed in the previous task

r = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")

soup = bs(r.content, features="lxml")
contents = soup.prettify()

#Search for a common class to extract every movielink
#Extract movielinks from each table representing a different decade
#Grab italicizeds elements from each table

movies = soup.select(".wikitable.sortable i")
print(movies[0].a['href'])
print(movies[0].a['title'])

#Now that the link and title has been grabbed, this can be turned into a function for the rest of the links
#Use the same function as before, but now an URL will be passed as an argument


def get_content_value(row_data):
    if row_data.find("li"):
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all('li')]
    elif row_data.find("br"):
        return [text for text in row_data.stripped_strings]
    else:
        return row_data.get_text(" ", strip=True).replace("\xa0", " ")

### First, cleaning up references [1], [2], etc. After inspecting the web page, removing the "sup" part is a possible solution
### A new function was added to get_info_box to clean the date before creating JSON doc again.
### remove = span, to remove extra information on realease date that we don't need

def clean_tags(soup):
    for tag in soup.find_all(["sup", "span"]):
        tag.decompose()

def get_info_box(url):

    r = requests.get(url)
    soup = bs(r.content, features="lxml")
    info_box = soup.find(class_ = "infobox vevent")
    info_rows = info_box.find_all("tr")

    clean_tags(soup)
    movie_info = {}

    for index, row in enumerate(info_rows):
        if index == 0:
            movie_info["title"] = row.find('th').get_text(" ", strip=True)
        elif index == 1:
            continue
        else:
            content_key = row.find("th").get_text(" ", strip=True)
            content_value = get_content_value(row.find("td"))
            movie_info[content_key] = content_value

    return movie_info

r = requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
soup = bs(r.content, features="lxml")
movies = soup.select(".wikitable.sortable i a")

#Create a for loop that iterates each URL passed to the function
#Create a full path to pass as an argument in move_info_list

base_path = "https://en.wikipedia.org/"

movie_info_list = []
for index, movie in enumerate(movies):
    try:
        path = movie['href']
        full_path = base_path + path
        title = movie['title']


        movie_info_list.append(get_info_box(full_path))
    except Exception as e:
        print(movie.get_text())
        print(e)
    

# It seems that some italicized elements are not links, but only text
# add "a" to the select method so as to avoid getting some of the items

print(movie_info_list[0])

### Now that everything is running smoothly, the date will be saved as a JSON file


#save_data("movie_data_set_clean.json", movie_info_list)

### Task 3: Cleaning data
# Convert runing time into interger
# Convert date into datetime objects
# strip the text: [1]
# Split up the long strips that were not listed

# Split long strips
#Example: "Starring": "Fess Parker Jeffrey Hunter John Lupton Jeff York Slim Pickens",
#After inspecting, "br" could be used to handle this and separate the items into a list
#Using the documentation on get_text(), a new elif  was added to or main function: stripped_strings

movie_info_list = load_data("movie_data_set_clean.json")

print([movie.get('Running time', 'N/A')for movie in movie_info_list])

# Create a function that only captures the time and converts it into an interger
# Also, the function needs to deal with lists

def minutes_to_interger(running_time):

    if running_time == "N/A":
        return None

    elif isinstance(running_time, list):
        entry = running_time[0]
        minutes = entry.split(" ")[0]
    
        return int(minutes)

    else:
        
        minutes = running_time.split(" ")[0]
        return int(minutes)

for movie in movie_info_list:
    movie[ 'Running time'] = minutes_to_interger(movie.get('Running time', 'N/A'))
print(movie_info_list[10])

### Date conversion
# Analyzing the data pattern and format
# Most common pattern example: "June 28, 1950"
dates = ([movie.get('Release date', 'N/A')for movie in movie_info_list])

from datetime import datetime

def clean_date(date):
    return date.split("(")[0].strip()

def date_conversion(date):
    if isinstance(date, list):
        date = date[0]

    if date == 'N/A':
        return None
    
    date_str = clean_date(date)

    # there are several date formats that need to be taken into account
    formats = ["%B %d %Y", "%d %B %Y"]
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except:
            pass

    return None
print(dates)

import json

def save_data(title, data):
    with open(title, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(title):
    with open(title, encoding='utf-8') as f:
        return json.load(f)

save_data("movie_data_set_clean_final.json", movie_info_list)








