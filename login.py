# Maria Jose Castro - 181202
# Proyecto Cliente XMPP
# Archivo del User options

# import ade librerias
import xmpp
import logging
import slixmpp
from slixmpp.exceptions import IqError, IqTimeout


class Login(slixmpp.ClientXMPP):
    # iniciar sesion
    def __init__(self, username, password):
        slixmpp.ClientXMPP.__init__(self, username, password)
        self.add_event_handler("session_start", self.session_login)
        self.add_event_handler("menu", self.menu)

    def session_login(self, event):
      self.send_presence('chat', 'Login')
      self.get_roster()

    def menu(self):
      print('hola')
      try:
        input('inset new number')
        #self.disconnect()
        hola = 1+1
        print(hola)
      except IqError as e:
        print('eerrir')

