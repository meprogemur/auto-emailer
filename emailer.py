import os
import smtplib
from email.message import EmailMessage
import requests
import random

EMAIL_PASS = os.environ.get('DEFAULT_EMAIL_PASSWORD')
EMAIL_USER = os.environ.get('DEFAULT_EMAIL_USER')
EMAIL_TO = os.environ.get('DEFAULT_EMAIL_TO')
kwargs = ['cuddle', 'love', 'kiss+her', 'hug+her', 'pat+her', 'poke+her', 'slap+her', 'tickle+her', 'carry+her']
q = random.choice(kwargs)
print(q)
url = f'https://api.giphy.com/v1/gifs/search?api_key=KKPAYCiPWBvoDdRTMvbSoJPigM11E0g9&q={q}&limit=25&offset=0&rating=g&lang=en'
something = "something"
response = requests.get(url)
data = response.json()
data = data['data']
data = random.choice(data)
data = data['images']['original']['url']
print(data) 
pickup = requests.get('http://getpickuplines.herokuapp.com/lines/random')
pickup = pickup.json()
pickup = pickup['line']
print(pickup)
msg = EmailMessage()
msg['Subject'] = 'Hiii Boibbyyyy!'
msg['From'] = EMAIL_USER
msg['To'] = EMAIL_TO
msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
    <body>
    <h1 style="color:gray">{pickup}</h1>
    <img src="{data}" alt="yes">
    </body>
    </html>
    """,subtype='html')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_USER, EMAIL_PASS)

    # msg = "Subject: saxy\n\nbooty" 
    smtp.send_message(msg)