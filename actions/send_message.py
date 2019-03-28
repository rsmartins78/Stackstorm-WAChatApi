from sender.wa_sender import WhatsAppChatApiMessages
from emoji import emojize
from st2common.runners.base_action import Action


class WhatsappSendMessageAction(Action):
    def run(self, chat_id, message):
        wa = WhatsAppChatApiMessages(server=self.config['api_server'],instance=self.config['api_instance'],api_token=self.config['api_token'])
        message = wa.send_message(chat_id=chat_id,message=emojize(message,use_aliases=True))
        return message

