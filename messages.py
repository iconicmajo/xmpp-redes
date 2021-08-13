# Maria Jose Castro - 181202
# Proyecto Cliente XMPP
# Archivo para mandar y recibir mensages

# Import de Librerias
import xmpp
import slixmpp
import threading
from slixmpp.clientxmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout

import time

"""
************************
ESPANOL
************************
DENTRO DE ESTE ARCHIVO SE HARA TODAS LAS ACCIONES CORRESPONDIENTES
A LOS MENSAJES ENTRE ESTOS ESTAN 
-PRESENCIA
-ENVIAR MENSAJE
-RECIBIR MENSAJE

************************
ENGLISH
************************
INSIDE THIS FILE YOU WILL FIND ALL THE FUNCTIONS NEEDED FOR MESSAGE ACTIONS
THE ACTIONS ARE
-PRESENCE MESSAGE
-RECIVE MESSAGE
-SEND MESSAGE
"""


# Enviar Mensaje Privado
class PrivateMessage(ClientXMPP):
    def __init__(self, user, password, user_destiny, message):
        ClientXMPP.__init__(self, user, password)
        self.user_destiny = user_destiny
        self.msg = message

        self.add_event_handler("session_start", self.session_login)
        #self.add_event_handler("logout", self.send_message)

    def session_login(self, event):
        self.send_presence('chat', 'sendin message!')
        self.get_roster()
        self.send_message(mto=self.user_destiny,
                          mbody=self.msg,
                          mtype='chat')
        print('Message Send!')
        self.disconnect(wait=False)

#Enviar mensaje de presencia
class PesenceMessage(ClientXMPP):
    def __init__(self, user, password, message):
        ClientXMPP.__init__(self, user, password)
        self.add_event_handler("session_start", self.session_login)
        self.presence = threading.Event()
        self.contacts = []

    def session_login(self, event):
        self.send_presence('chat', 'hola')
        self.get_roster()

        self.presence.wait(3)

        print('enviado')
        self.disconnect()
        #self.send_pres()

    
    def send_pres(self, show, status):
        print('')
        self.send_presence(show, status)
        self.get_roster()
        time.sleep(3)
        print('Message Send!')



#Enviar mensaje de presencia