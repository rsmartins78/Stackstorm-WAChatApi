import requests

class WhatsAppChatApiMessages:

    def __init__(self, server, instance, api_token):
        self.server = server
        self.instance = instance        
        self.api_token = api_token

    def send_message(self,chat_id,message):

        url = "https://"+self.server+".chat-api.com/"

        data = {'chatId':chat_id, 'body':message}

        r = requests.post(url=url+str(self.instance)+'/sendMessage?token='+str(self.api_token), json=data)

        response_text = r.text

        print(response_text)