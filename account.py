# Maria Jose Castro - 181202
# Proyecto Cliente XMPP
# Archivo del User options

# import ade librerias
import xmpp


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
def login():
		print(' ')
		print('You Choose Login')
		userName = input('user:  ')
		passWord = input('password: ')
		user = userName
		psswrd = passWord
		#print(user+' '+ psswrd)
		# xmpp.process(forever=True)
		# return xmpp

#cerrar sesion
def logout():
		print(' ')
		print('You Choose Logout')
		#userName = input('user:  ')
		passWord = input('password: ')
		user = userName
		psswrd = passWord
		#print(user+' '+ psswrd)
		# xmpp.process(forever=True)
		# return xmpp

#Eliminar la cuenta	 
def deleteAccount():
		print(' ')
		print('You Choose Delete Account')
		userName = input('user:  ')
		passWord = input('password: ')
		user = userName
		psswrd = passWord
		#print(user+' '+ psswrd)
		# xmpp.process(forever=True)
		# return xmpp
