
import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.se/-/en/PATHFINDER-CORE-RULEBOOK-HC-P2/dp/1640781684/ref=sr_1_2?keywords=pathfinder+2e&qid=1674153432&sprefix=path%2Caps%2C132&sr=8-2'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Getting the title of the product as well as trimming the white space before and after
    title = soup.find(id = 'productTitle').get_text().strip()

    # Getting the price of the product,converting to a float and taking only the part we need
    price = soup.find('span', {'class': 'a-price-whole'}).get_text()
    converted_price = float(price[:3])

    if(converted_price < 400):
        send_email()

# Setting up a conection in order to send an email

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gastonsuarezm@gmail.com', 'ndtkwbuhxgwxcovs')
    subject = 'Price drop!'
    body = 'Check the link https://www.amazon.se/-/en/PATHFINDER-CORE-RULEBOOK-HC-P2/dp/1640781684/ref=sr_1_2?keywords=pathfinder+2e&qid=1674153432&sprefix=path%2Caps%2C132&sr=8-2'  

    message = f"Subject: {subject}\n\n {body}"
    #From, to and the message
    server.sendmail(
        'gastonsuarezm@gmail.com',
        'gastonsuarezm@gmail.com',
        message
    )
    print('Email has been sent')
    server.quit

# Adding a while loop so that the functions only runs once a day
while(True):
    check_price()
    time.sleep(86400)

