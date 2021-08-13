# Maria Jose Castro - 181202
# Proyecto Cliente XMPP
# Archivo para mandar y recibir mensages

# Import de Librerias
import xmpp
import slixmpp

# Enviar Mensaje Privado


class PrivateMessage(slixmpp.ClientXMPP):
    def __init__(self, user, password, user_destiny, message):
        slixmpp.ClientXMPP.__init__(self, user, password)
        self.user_destiny = user_destiny
        self.msg = message


    async def start(self, event):
        # Send presence
        self.send_presence()
        await self.get_roster()

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    # Send message of type chat
        self.send_message(mto=self.user_destiny,
                          mbody=self.msg,
                          mtype='chat')

    def message(self, msg):
        # Print message
        if msg['type'] in ('chat'):
            user_destiny = msg['to']
            body = msg['body']

            # print the message and the user_destiny
            print(str(user_destiny) + ": " + str(body))

            # Ask new message
            message = input("Write the message: ")

            # Send message
            self.send_message(mto=self.user_destiny,
                              mbody=message)

    '''def privateMsg(self, message):
        print(' ')
        print('Yout Choose Private Message')

        self.send_presence()
        await self.get_roster()
        send_message()
        # xmpp.connect()'''

# Enviar Mensaje de Presencia


def presenceMessage():
    print(' ')
    print('Yout Choose Presence Message')
    message = input('Message of Presence: ')
    print(message)

# Recibir mensaje


def getMessage():
    print(' ')
    print('Yout Choose Get Message')
