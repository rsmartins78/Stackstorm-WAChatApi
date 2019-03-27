import requests

class whatsappchatapi:

    def send_message(instance,token,chat_id,message):

        url = "https://eu21.chat-api.com/"

        api_instance = instance

        data = {'chatId':str(chat_id), 'body':str(message)}

        r = requests.post(url=url+str(api_instance)+'/sendMessage?token='+str(token), json=data.encode('utf8'))

        response_text = r.text
        
        print(response_text)