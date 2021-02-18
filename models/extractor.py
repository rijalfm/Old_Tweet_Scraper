import json, re
from time import strftime, localtime
from datetime import datetime, timezone

def utc_to_local(utc_dt):
	return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def extract_json(data):
	data = json.loads(data)
	tweets = data['globalObjects']['tweets']
	users = data['globalObjects']['users']
	tweets_id = set(tweets.keys())

	return tweets, users, tweets_id

def extract_tweet(_id, tweets, users, _json=False):
	tw = tweets[_id]
	user_id = tw['user_id_str']
	uData = users[user_id]

	# User Information
	
	username = uData['screen_name']
	full_name = uData['name']
	avatar = uData['profile_image_url_https']
	followers = uData['followers_count']
	verified = uData['verified']

	_dt = tw['created_at']
	_dt = datetime.strptime(_dt, '%a %b %d %H:%M:%S %z %Y')
	_dt = utc_to_local(_dt)
	_datetime = str(_dt.strftime('%d-%b-%Y %H:%M:%S'))

	place = tw['place']['full_name'] if tw['place'] else ''
	try:
		source = re.findall(r'>[a-zA-Z0-9 ]+', tw['source'])[0][1:] if tw['source'] else ''
	except:
		source = ''
	try:
		mentions = [_mention['screen_name'] for _mention in tw['entities']['user_mentions']]
	except KeyError:
		mentions = []
	try:
		urls = [_url['expanded_url'] for _url in tw['entities']['urls']]
	except KeyError:
		urls = []
	try:
		photos = [_img['media_url_https'] for _img in tw['entities']['media'] if _img['type'] == 'photo' and
								_img['expanded_url'].find('/photo/') != -1]
	except KeyError:
		photos = []
	try:
		video = 1 if len(tw['extended_entities']['media']) else 0
	except KeyError:
		video = 0
	try:
		hashtags = [hashtag['text'] for hashtag in tw['entities']['hashtags']]
	except KeyError:
		hashtags = []

	tweet = tw['full_text']

	lang = tw['lang']

	replies_count = tw['reply_count']
	retweets_count = int(tw['retweet_count']) + int(tw['quote_count'])
	likes_count = tw['favorite_count']
	link = f"https://twitter.com/{username}/status/{_id}"
	reply_to = tw['in_reply_to_screen_name'] if tw['in_reply_to_screen_name'] else ''
	try:
		quote_url = tw['quoted_status_permalink']['expanded'] if tw['is_quote_status'] else ''
		quote_from = re.findall(r'\/[a-zA-Z0-9_-]+/',quote_url)
		if len(quote_from) > 0:
			quote_from = quote_from[0][1:-1]
		else:
			quote_from = ''
	except KeyError:
		quote_url = 0
		quote_from = ''

	try:
		print(f'[{_datetime}] {username}')
	except:
		pass
	
	if _json:
		data_tweet = {'date': _datetime,
						'username': username,
						'fullname': full_name,
						# 'avatar': avatar,
						'verified': verified,
						'followers': followers,
						'id': _id,
						'replies': replies_count,
						'retweets': retweets_count,
						'favorites': likes_count,
						'tweet': tweet,
						'mentions': mentions,
						'hashtags': hashtags,
						'permalink': link,
						'replyTo': reply_to,
						'quoteUrl': quote_url,
						'quoteFrom': quote_from,
						'photos': photos,
						'lang': lang,
						'source': source,
						'place': place}

		if _json:
			return data_tweet