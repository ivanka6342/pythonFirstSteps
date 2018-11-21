import telepot
#import sys
#import python-telegram-bot
import requests
import json
import botToken

requestLine = 'https://api.telegram.org/bot' + botToken.token + '/'

def init_bot():
	return telepot.Bot(botToken.token)

def get_updates():
	req = requestLine + 'getUpdates'
	result = requests.get(req)
	return result.json()

def get_message():
	data = get_updates()
	chat_id     = data['result'][-1]['message']['chat']['id']
	sender_name = data['result'][-1]['message']['from']['username']
	message = { 'chat_id'      : chat_id,
				'sender_name'  : sender_name }
	return message

def send_message(chat_id, sender_name):
	req = requestLine + 'sendMessage?chat_id={}&text={}'.format(chat_id, sender_name + ', U R 64Y')
	requests.get(req)

def main():
	last_msg = get_message()
	send_message(last_msg['chat_id'], last_msg['sender_name'])
	#d = getUpdates()
	#with open('dumpJSONrequest.txt', 'w') as f:
	#	json.dump(d, f, indent = 2, ensure_ascii = False)

if __name__ == '__main__':
	main()
