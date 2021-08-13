# Maria Jose Castro - 181202
# Proyecto Cliente XMPP
# Archivo del User options

# import ade librerias
from slixmpp.clientxmpp import ClientXMPP
import xmpp
import logging
import slixmpp
from slixmpp.exceptions import IqError, IqTimeout

"""
************************
ESPANOL
************************
DENTRO DE ESTE ARCHIVO SE HARA TODAS LAS ACCIONES CORRESPONDIENTES
A LA CUENTA DEL USUARIO, AQUI ESTARA ELIMINAR, CREAR, INGRESAR Y SALIR.
CREAR USUARIO ES LA UNICA FUNCION DECLARADA COMO TAL Y NO COMO CLASE

LAS FUNCIONES COMO CLASE NECESITAN INGRESAR A LA CUENTA ANTES DE HACER
LA ACCION

************************
ENGLISH
************************

INSIDE THIS FILE YOU WILL FIND ALL THE FUNCTIONS NEEDED FOR USER ACTIONS, 
THE ACTIONS ARE CREATE, DELETE, LOGIN AND LOGOUT
THE CREATE IS THE ONLY REAL FUNTION, THE OTHERS ARE CLASS TYPED.

THE CLASS TYPED NEEDS TO LOGING THE SERVER BEFORE ALL ACTIONS"""

# Creacion de usuario
def createUser():
		print(' ')
		print('You Choose Create User')
		new_user = input('username@alumchat.xyz:  ')
		new_password = input('password:  ')
		user = new_user
		password = new_password
		jid = xmpp.JID(user)
		cli = xmpp.Client(jid.getDomain(), debug=[])
		cli.connect()
		if xmpp.features.register(cli, jid.getDomain(), {'username': jid.getNode(), 'password': password}):
				return True
		else:
				return False


# iniciar sesion
class Login(slixmpp.ClientXMPP):
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
				hola = 1+1
				print(hola)
			except IqError as e:
				print('eerrir')

# cerrar sesion
class AccountLogout(ClientXMPP):
		def __init__(self, user, password):
				ClientXMPP.__init__(self, user, password)
				self.add_event_handler("session_start", self.session_logout)
				self.add_event_handler("logout", self.logout)

		def session_logout(self, event):
				self.send_presence('chat', 'bye!')
				self.get_roster()
				self.disconnect(wait=False)

		def logout(self):
				self.disconnect(wait=False)


# Eliminar la cuenta
class AccountDelete(ClientXMPP):
		def __init__(self, user, password):
			ClientXMPP.__init__(self, user, password)
			self.add_event_handler("session_start", self.session_login)
			self.add_event_handler("logout", self.deleteUser)

		def session_login(self, event):
			self.send_presence('chat', 'Account about to delete')
			self.get_roster()

		def deleteUser(self):
						resp = self.Iq()
						resp['type'] = 'set'
						resp['from'] = self.boundjid.full
						resp['register']['remove'] = True

						try:
								resp.send(True)
								print("User Deleted")

						except IqError as err:
								print("Delete Process Failed")
								self.disconnect()

						except IqTimeout:
								print("Session Timeout")
								self.disconnect()
