import requests
from sys import stderr
from json import loads, load
from time import sleep

def work():
	for i in range(len(workers) - 1, -1, -1):
		worker = workers[i]
		r = requests.get(f'https://api.telegram.org/bot{worker.tg_tkn}/getUpdates?offset=-1')
		print('Last channel ID:')
		print(r.json()['result'][0]['message']['chat']['id'])
		try:
			print(f'The bot has been successfully launched, waiting for new posts.')
		except Exception as error:
			print(f'Error: {error}\n {r.json()}')
			del workers[i]

		check_posts(workers)


def check_posts(workers):
	while True:
		for worker in workers:
			try:
				for channel in worker.ds_chids:
					r = requests.get(f'https://discord.com/api/v9/channels/{channel}/messages?limit=1', headers={'authorization': worker.ds_tkn})
					new_msg_id = loads(r.text)[0]['id']
					if worker.ds_chids[channel] == 0 or int(worker.ds_chids[channel]) != int(new_msg_id):
						msg_text = loads(r.text)[0]['content']
						msg_author = loads(r.text)[0]['author']['username']
						msg_attachments = loads(r.text)[0]['attachments']
						if worker.ds_chids[channel] != 0:
							print('A new post. The information was successfully sent to Telegram')
							if len(msg_text) > 0:
								post = requests.post(f'https://api.telegram.org/bot{worker.tg_tkn}/sendMessage',
											json={'chat_id': worker.chat_id, 'text': f'#{str(msg_author).replace(" ", "_")}\n\n{str(msg_text)}'})
								if msg_attachments:
									msg = loads(post.text)
									msg_id = msg['result']['message_id']
									for attachment in msg_attachments:
										requests.post(f'https://api.telegram.org/bot{worker.tg_tkn}/sendPhoto',
											json={'chat_id':  worker.chat_id, 'photo': str(attachment['url']), 'reply_to_message_id': int(msg_id)})
								sleep(1)
						worker.ds_chids[channel] = new_msg_id
			except Exception as error:
				print(error)
				pass

f = open('cfg.json')
data = load(f)
f.close()

class Worker:
	def __init__(self, tg_tkn, ds_tkn, ds_chids, chat_id):
		self.tg_tkn = tg_tkn
		self.ds_tkn = ds_tkn
		self.ds_chids = ds_chids
		self.chat_id = chat_id

workers = []

for i in data['accounts']:
	workers.append(Worker(i['tg_botkey'], i['ds_token'], i['ds_channels'], i['tg_chat']))

work()
