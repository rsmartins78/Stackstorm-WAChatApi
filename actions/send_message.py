from sender.wa_sender import WASendMessage
from emoji import emojize
from st2common.runners.base_action import Action


class WhatsappSendMessageAction(Action):
    def run(self, chatId, message):
        message = WASendMessage.send_message(instance=self.config['instance'],token=self.config['api_token'],chatId=chatId,message=emojize(message, use_aliases=True))
        return message

