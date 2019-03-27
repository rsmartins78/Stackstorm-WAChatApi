#!/usr/bin/env python

import requests

class WASendMessage:

    def send_message(instance,token,chatId,message):

        url = "https://eu21.chat-api.com/"

        data = {'chatId':chatId, 'body':message}

        r = requests.post(url=url+instance+'/sendMessage?token='+token, json=data.encode('utf8'))

        response_text = r.text
        print(response_text)






# instance = "instance32573"
# token = "pkdahmmvixtcmajp"
# chatId = '5511952218967@c.us'
# message = 'Hello From Python'

# send_message(instance,token,chatId,message)