import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Yamaha-Revstar-RSP20CR-Solidbody-Electric/dp/B01EXNTZ7I?ref_=ast_sto_dp"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:-3].replace(',', ''))

    if (converted_price < 1600):
        send_mail()

    print (converted_price)
    print (title.strip())

    if(converted_price > 1.600):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jondehlin@gmail.com', 'cfkasotflsdcialx')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Yamaha-Revstar-RSP20CR-Solidbody-Electric/dp/B01EXNTZ7I?ref_=ast_sto_dp'

    msg = "Subject: {}\n\n{}".format(subject, body)
    print (msg)
    # msg = "Hello"

    server.sendmail(
        'jondehlin@gmail.com',
        'dehlinjd@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_price()
    time.sleep(10)