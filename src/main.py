from dotenv import load_dotenv
import pyfiglet
import colorama
import os
import json

from bombers import EmailBomber


from twilio.rest import Client


def main():
	email_bomber = EmailBomber(os.environ["RECEIVER_EMAIL"], "Привет мир", msg="Hello", min_interval=5, max_interval=5)
	email_bomber.start_bombing(os.environ['SENDER_EMAIL'], os.environ['SENDER_EMAIL_PASSWORD'])



if __name__ == '__main__':
	load_dotenv('../.env')
	colorama.init()
	print(colorama.Fore.RED + pyfiglet.figlet_format("Bomber", font="slant"))
	print(colorama.Style.RESET_ALL)
	main()
