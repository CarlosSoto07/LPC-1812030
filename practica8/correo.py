import email, smtplib, ssl, getpass, imghdr, os

from email.message import EmailMessage

def enviarcorreo():
	subject = input("Introduzca el asunto del correo: ")
	body = input("Introduzca el mensaje del correo: ")
	sender_email = "sotocarlosadrian98@gmail.com"
	receiver_email = input("Introduzca el destinatario: ")
	password = getpass.getpass("Introduzca la contraseña:")

	# Create a multipart message and set headers
	message = EmailMessage()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject

	# Aqui se envia el correo electronico 
	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
	    server.login(sender_email, password)
	    server.send_message(message)
	print("Correo enviado con exito a: %s" % (receiver_email))

if __name__ =='__main__':
    enviarcorreo()