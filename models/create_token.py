import requests, re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}

class Token():
    def __init__(self):
        self.retries = 10
        self.url = 'https://mobile.twitter.com'
    
    def get_token(self):
        for attempt in range(self.retries):
            try:
                results = requests.get(self.url, headers=headers)
            except:
                results = None
            
            if results:
                break
        
        try:
            match = re.search(r'\("gt=(\d+);', results.text)
            return str(match.group(1))
        except:
            return None
