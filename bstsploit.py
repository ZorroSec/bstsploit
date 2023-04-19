import os
import time
import requests
from menu.menu import menu
from colorama import Fore, Style

while True:
	op = menu()
	if op == "bstsubprosses":
		print('funcionou!!')