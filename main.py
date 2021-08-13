#Maria Jose Castro - 181202
#Proyecto Cliente XMPP
#Archivo del main

#Import de librerias 
import sys 
import time 
import ssl
from account import *
from login import * 
from messages import *
#from slixmpp import ClientXMPP

"""
************************
ESPANOL
************************
DENTRO DE ESTE ARCHIVO SE TENDRA TOD O EL MAIN NECESARIO PARA CORRER EL 
ARCHIVO, AQUI SE IRAN LLAMANDO A TODAS LAS FUNCIONES NECESARIAS

************************
ENGLISH
************************

INSIDE THIS FILE YOU WILL THE MAIN FILE FOR THW WHOLE PROGRAM, HERE ARE THE CALLS 
FOR THE FUNTIONS NEEDED FOR USE

"""

menu = True
while menu:
    print('***********************')
    print('         CHAT          ')
    print('***********************')
    """print('1. Login')
    print('2. Create User')
    print('3. Send Private Message')
    print('4. See Users Info')
    print('5. Presence Message')
    print('6. See contact Info')
    print('7. Get Notifications')
    print('8. Send Files')
    print('9. Logout')
    print('10. Delete Account')
    print('')"""
    option = input('Please select an option: ')
    print(' ')

    if option == '1':
      print(' ')
      print('You Choose Login')
      username = input('user:  ')
      password = input('password: ')
      xmpp = Login(username, password)
      xmpp.register_plugin('xep_0030') # Service Discovery
      xmpp.register_plugin('xep_0199') # XMPP Ping
      xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
      xmpp.register_plugin('xep_0096') # Jabber Search
      xmpp.connect()
      xmpp.process(forever=False)

    elif option == '2':
      createUser()

    elif option == '3':
      username = input('user:  ')
      password = input('password: ')
      user_destiny = input('user@alumchat.xyz: ')
      message = input('Message: ')
      xmpp = PrivateMessage(username, password, user_destiny, message)
      xmpp.register_plugin('xep_0030') # Service Discovery
      xmpp.register_plugin('xep_0199') # XMPP Ping
      xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
      xmpp.register_plugin('xep_0096') # Jabber Search
      xmpp.connect()
      xmpp.process(forever=False)

    elif option == '4':
      print('option 4')
      
    elif option == '5':
      print(' ')
      username = input('user:  ')
      password = input('password: ')
      message = input('Message: ')
      xmpp = PesenceMessage(username, password, message)
      xmpp.register_plugin('xep_0030') # Service Discovery
      xmpp.register_plugin('xep_0199') # XMPP Ping
      xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
      xmpp.register_plugin('xep_0096') # Jabber Search
      xmpp.connect()
      xmpp.process(forever=False)

    elif option == '6':
      print('option 6')

    elif option == '7':
      print('option 7')

    elif option == '8':
      print('option 8')

    elif option == '9':
      print(' ')
      username = input('user:  ')
      password = input('password: ')
      xmpp = AccountLogout(username, password)
      xmpp.register_plugin('xep_0030') # Service Discovery
      xmpp.register_plugin('xep_0199') # XMPP Ping
      xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
      xmpp.register_plugin('xep_0096') # Jabber Search
      xmpp.connect()
      xmpp.process(forever=False)

    elif option == '10':
      username = input('user:  ')
      password = input('password: ')
      xmpp = AccountDelete(username, password)
      xmpp.register_plugin('xep_0030') # Service Discovery
      xmpp.register_plugin('xep_0199') # XMPP Ping
      xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
      xmpp.register_plugin('xep_0096') # Jabber Search
      xmpp.connect()
      xmpp.process(forever=False)










