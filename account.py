#Maria Jose Castro - 181202
#Proyecto Cliente XMPP
#Archivo del User options

#import ade librerias 
import xmpp


#Creacion de usuario
def createUser(new_user, new_password):
    user = new_user
    password = new_password
    jid = xmpp.JID(user)
    cli = xmpp.Client(jid.getDomain(), debug=[])
    cli.connect()

    if xmpp.features.register(cli, jid.getDomain(), {'username': jid.getNode(), 'password': password}):
        return True
    else:
        return False 

#iniciar sesion