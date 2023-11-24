from dotenv import load_dotenv
import pyfiglet
import colorama
import os

from email_bomber import EmailBomber


def main():



if __name__ == '__main__':
	load_dotenv('../.env')
	colorama.init()
	print(colorama.Fore.RED + pyfiglet.figlet_format("Bomber", font="slant"))
	print(colorama.Style.RESET_ALL)
	main()
