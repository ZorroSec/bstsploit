import os
import time
import requests
from menu.menu import menu
from colorama import Fore, Style

op = input(menu())
if op == "exit":
	exit()