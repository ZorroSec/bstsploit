import os
import time
import requests
from menu.menu import menu
import sys
from colorama import Fore, Style

try:
	op = input(menu())
	if op == "exit":
		sys.exit()
except KeyboardInterrupt:
	print(f"{Fore.RED}Saindo...{Style.RESET_ALL}")
