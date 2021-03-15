import smtplib
import ssl
import json
import random
import string


def generate_random_string():
    random_string = ''
    letters = string.ascii_letters
    for i in range(random.randint(5, 10)):
        random_string += random.choice(letters)
    return random_string


with open('settings.json') as f:
    data = json.load(f)

port = 465

context = ssl.create_default_context()

while True:
    for username, password in zip(data['username'], data['password']):
        for recipient in data['recipient']:
            with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
                try:
                    server.login(username, password)
                except smtplib.SMTPAuthenticationError:
                    print('Issues signing in')
                    input('Press enter to close')
                    quit()
                server.sendmail(username, recipient, 'Subject: {}\n\n{}'.format(generate_random_string(),
                                                                                data['message']))
