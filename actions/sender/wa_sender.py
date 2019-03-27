import requests


def wasend_message(instance,token,chat_id,message):

    url = "https://eu21.chat-api.com/"

    data = {'chatId':chat_id, 'body':message}

    r = requests.post(url=url+str(instance)+'/sendMessage?token='+str(token), json=data)

    response_text = r.text

    print(response_text)