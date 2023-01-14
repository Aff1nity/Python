
#Import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

URL = 'https://www.goodreads.com/list/show/35446.The_Grimdarks'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content , "html.parser")

#Checking that it is working

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

#Let's get the title

book_titles = soup2.select('.bookTitle')
print(book_titles)

#Creating an empty list to store the first 100 book titles of the first page
titles = []

for title in book_titles:

    titles.append(title.get_text())

#Checking that the for loop retrive the correct information
#print(titles)

# Since the elements have empty spaces, we should remove them so that we only
# the information that we want
titles = list(map(str.strip, titles))
print(titles)

# Use the enumerate function to add an index to the list of book titles
# so that we can have the complete list with the first 100 books of this particular list 
# of Grimdark books on Goodreads
for index, title in enumerate(titles):
    print(index + 1, title)



