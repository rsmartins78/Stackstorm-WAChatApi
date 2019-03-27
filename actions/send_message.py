from sender.wa_sender import wasend_message
from emoji import emojize
from st2common.runners.base_action import Action


class WhatsappSendMessageAction(Action):
    def run(self, chat_id, message):
        message = wasend_message(instance=self.config['api_instance'],token=self.config['api_token'],chat_id=chat_id,message=emojize(message,use_aliases=True))
        return message

