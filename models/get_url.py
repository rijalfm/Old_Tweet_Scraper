from urllib.parse import urlencode
from urllib.parse import quote

class URL:
	def __init__(self):
		self.base_url = 'https://api.twitter.com/2/search/adaptive.json'
		self.tweet_count = 100

	def url_parser(self, query, init):
		params = [
      # ('include_blocking', '1'),
      # ('include_blocked_by', '1'),
      # ('include_followed_by', '1'),
      # ('include_want_retweets', '1'),
      # ('include_mute_edge', '1'),
      # ('include_can_dm', '1'),
      ('include_can_media_tag', '1'),
      # ('skip_status', '1'),
      # ('include_cards', '1'),
      ('include_ext_alt_text', 'true'),
      ('include_quote_count', 'true'),
      ('include_reply_count', '1'),
			('tweet_mode', 'extended'),
			('include_entities', 'true'),
			('include_user_entities', 'true'),
			('include_ext_media_availability', 'true'),
			('send_error_codes', 'true'),
			('simple_quoted_tweet', 'true'),
			('count', self.tweet_count),
			# ('query_source', 'typed_query'),
			# ('pc', '1'),
			('cursor', str(init)),
			('spelling_corrections', '1'),
			('ext', 'mediaStats%2ChighlightedLabel'),
			('tweet_search_mode', 'live'),  # this can be handled better, maybe take an argument and set it then
			('f', 'tweets'),
			("l", 'id'),
			("lang", "en"),
			("q", query)
		]

  	# Final URL
		url = self.base_url + '?' + urlencode(params, quote_via=quote)
		return url