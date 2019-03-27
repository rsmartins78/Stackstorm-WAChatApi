import requests

class whatsappchatapi:

    def send_message(instance,token,chat_id,message):

        url = "https://eu21.chat-api.com/"

        data = {'chatId':chat_id, 'body':message}

        r = requests.post(url=url+instance+'/sendMessage?token='+token, json=data.encode('utf8'))

        response_text = r.text
        print(response_text)