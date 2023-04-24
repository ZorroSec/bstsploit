import socket
from colorama import Fore, Style

target = input(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}target{Fore.LIGHTWHITE_EX}]>{Style.RESET_ALL}')
choose = input(f'{Fore.LIGHTWHITE_EX}Do you want to add a predefined port?{Fore.LIGHTGREEN_EX}Y{Fore.LIGHTBLACK_EX}/{Fore.LIGHTRED_EX}N{Style.RESET_ALL}')
if choose == 'y' or 'Y':
    port = input(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}port{Fore.LIGHTWHITE_EX}]>{Style.RESET_ALL}')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.05)
    if s.connect_ex((target, port)) == 0:
        print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}port{Fore.LIGHTWHITE_EX}]>{Style.RESET_ALL}')
elif choose == 'n' or 'N':
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        
        if s.connect_ex((target, port)) == 0:
            print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTGREEN_EX}port{Fore.LIGHTWHITE_EX}]>{Style.RESET_ALL}{port}')
        else:
            print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}port{Fore.LIGHTWHITE_EX}]>{Style.RESET_ALL}{port}')