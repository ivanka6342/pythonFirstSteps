import telepot
#import sys
#import python-telegram-bot
import requests
import json
import botToken

token = botToken.token
requestLine = 'https://api.telegram.org/bot' + token + '/'

def init_bot():
	with open('token.txt', 'r') as tokenFile:
		botToken = tokenFile.read()
	return telepot.Bot(botToken)

def get_updates():
	req = requestLine + 'getUpdates'
	result = requests.get(req)
	return result.json()

def get_message():
	data = get_updates
	chat_id = data['result'][-1]['message']['chat']['id']
	msg_text = data['result'][-1]['message']['text']
	message = { 'chat_id' : chat_id, 
				'message_text' : msg_text }
	return message

def send_message(chat_id, msg_text='dafault text'):
	req = requestLine + 'sendMessage?chat_id={}&text={}'.format(chat_id, msg_text)
	requests.get(req)

def main():
	answer = get_message()
	chat_id = answer['chat_id']
	send_message(chat_id)
	#d = getUpdates()
	#with open('dumpJSONrequest.txt', 'w') as f:
	#	json.dump(d, f, indent = 2, ensure_ascii = False)

if __name__ == '__main__':
	main()
