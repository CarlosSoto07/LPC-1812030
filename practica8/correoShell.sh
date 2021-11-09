from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import sys

if __name__ == '__main__':
    print(sys.argv)

data = {}
with open('pass.json') as f:
        data = json.load(f)
# create message object instance
msg = MIMEMultipart()

message = "Enviando mensaje desde script de bash"

msg['From'] = data['user']
receipents = ["sotocarlosadrian98@gmail.com"]
msg['To'] = ", ".join(receipents)
msg['Subject'] = "Carlo"

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com:465')

server.starttls()

server.login(data['user'], data['pass'])

server.sendmail(msg['From'], receipents, msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))