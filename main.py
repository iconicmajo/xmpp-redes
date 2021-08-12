#Maria Jose Castro - 181202
#Proyecto Cliente XMPP
#Archivo del main

#Import de librerias 
import sys 
import time 
import ssl
from account import *
#from slixmpp import ClientXMPP

while True:
    print('***********************')
    print('       CHAT REDES      ')
    print('***********************')
    print('1. Login')
    print('2. Create User')
    print('3. Send Private Message')
    print('4. Send Brodcast Message')
    print('5. Presence Message')
    print('6. See contact Info')
    print('7. Get Notifications')
    print('8. Send Files')
    print('9. Logout')
    print('10. Delete Account')
    print('')
    option = input('Please select an option: ')

    if option == '1':
      print('aun no sirve')
      login()

    elif option == '2':
      createUser()

    elif option == '3':
      print('option 3')

    elif option == '4':
      print('option 4')
      
    elif option == '5':
      print('option 5')

    elif option == '6':
      print('option 6')

    elif option == '7':
      print('option 7')

    elif option == '8':
      print('option 8')

    elif option == '9':
      print('option 9')
      logout()

    elif option == '10':
      print('option 10')
      deleteAccount()










