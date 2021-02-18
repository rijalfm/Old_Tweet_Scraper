# -*- coding: utf-8 -*-
"""To use this script you can pass the following attributes:
			 querysearch: a query text to be matched [using basic Twitter Advaned Search Query]
					foldername: saved results to this folder (./root/data/foldername)
					 limited: default (False), used for limit the number of tweets that you will scrape
				 maxtweets: default (100), if limited activated this number refer to the number of tweets that can scrape

Examples:
1. TweetScraper.py --querysearch "Politics" --foldername "politics"
2. TweetScraper.py --querysearch "(\\"Donald Trump\\" OR \\"Joe Biden\\") lang:id since:2020-12-30" --foldername "politics"
3. TweetScraper.py --querysearch "Politics" --foldername "politics" --limited
4. TweetScraper.py --querysearch "Politics" --foldername "politics" --limited --maxtweets 200
"""
import sys, re, os, time, getopt, json, requests
from datetime import datetime
from models import extractor
from models.get_url import URL
from models.create_token import Token

class Config:
	def __init__(self):
		self.foldername = os.path.join(os.getcwd(),"data")
		self.limited = False
		self.limit = 100
		self.query = ''
		self.cursor = '-1'
		self.tweets_id = []
		self.number_of_attempts = 2
		self.number_of_requests = 1
		self.number_of_tweets = 1
		self.Guest_token = Token().get_token()
		self.bearer = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs' \
									'%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'

config = Config()

def main(argv):

	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return

	if len(argv) == 1 and argv[0] == '-h':
		print(__doc__)
		return

	try:
		opts, args = getopt.getopt(argv, "", ("querysearch=",
																					"limited",
																					"maxtweets=",
																					"foldername="))
		for opt, arg in opts:

			if opt == '--querysearch':
				config.query = arg

			elif opt == '--maxtweets':
				config.limit = int(arg)

			elif opt == '--foldername':
				config.foldername = os.path.join(config.foldername,arg)

			elif opt == '--limited':
				config.limited = True


			if not os.path.exists(config.foldername):
				os.mkdir(config.foldername)

		while True:
			# Refresh Token
			if config.number_of_requests%10 == 0:
				config.Guest_token = Token().get_token()

			# Final URL
			url = URL().url_parser(config.query, config.cursor)

			# Requests Headers
			headers = {'authorization':config.bearer, 'x-guest-token':config.Guest_token,
								'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

			for _ in range(config.number_of_attempts):
				try:
					Get = requests.get(url, headers=headers)
				except:
					Get = None

				if Get:
					config.number_of_requests += 1
					break

			data_tweet = Get.text

			try:
				new_cursor = re.findall(r'scroll:[a-zA-Z0-9\-\_]+',str(data_tweet))[0]
			except:
				pass

			tweets, users, tweets_id = extractor.extract_json(data_tweet)

			for ids in tweets_id:
				if ids not in config.tweets_id:
					
					if config.limited and config.number_of_tweets > config.limit:
						break

					config.tweets_id.append(ids)            
					print(config.number_of_tweets, end=' - ')
					config.number_of_tweets += 1
					tweet = extractor.extract_tweet(_id=ids, tweets=tweets, users=users, _json=True)
					current_time = datetime.strftime(datetime.now(),"%d%m%Y%H%M%S")
					filename = os.path.join(config.foldername, f"{current_time}_{ids}.json")
					
					with open(filename, "w+", encoding="utf-8") as f:
						json.dump(tweet, f)

			if config.limited and config.number_of_tweets > config.limit:
				break

			if config.cursor == new_cursor:
				break
			else:
				config.cursor = new_cursor

	except Exception as err:
		print(err)

if __name__ == '__main__':
	main(sys.argv[1:])
