from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
import request
import json


auth_token = '4bdaa3514de7d042-8f5e1a8bfbfbaff7-57b58541fc7233b1'
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}


# sen is the body of the request to send to the viber backend servers
#seen, delivered - can be removed, but sometimes marketers want to know
# how much and who exactly received and read your messages, you can leave)

sen = dic(url='http://127.0.0.1:8000/webhook2020', event_types=['unsubscribed', 'conversation_started', 'message', 'seen', 'delivered'])


# r is a post request made according to the requirements of viber
r = request.POST(hook, json.dumps(sen), headers=headers)



# in the response print we should see "status_message": "ok" - which means
# that the webhook is installed
print(r.json())
