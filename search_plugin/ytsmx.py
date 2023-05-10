# VERSION: 1.1
# subzero

#!/usr/bin/env python3

from helpers import download_file, retrieve_url
from novaprinter import prettyPrinter
import json
from collections import defaultdict

class ytsmx(object):
	url = 'https://yts.mx/'
	api_url = 'http://yts.mx/api/v2/'
	name = 'yts.mx'
	supported_categories = {'movies':'6'}
	
	def __init__(self):
		print("======================")
	
	def download_torrent(self, info):
		pass

	def search(self, what, cat='all'):
		end_point = 'list_movies.json?'
		search_result = retrieve_url(self.api_url+end_point+'sort=seed&query_term='+what)
		search_result_parsed = json.loads(search_result)
		if search_result_parsed['status'] != 'ok':
			print('[ERR] %s' % search_result_parsed['status_message'])
			return 
		if search_result_parsed['data']['movie_count'] == 0:
			print("[FAILED] No movie was found")
			return 
		
		for movie in search_result_parsed['data']['movies']:
			for torrent in movie['torrents']:
				result = defaultdict(lambda:-1)
				result['link'] = torrent['url']
				result['name'] = ('%s %s' % (movie['title'], torrent['type']))
				result['size'] = torrent['size']
				result['seeds'] = torrent['seeds']
				result['engine_url'] = self.url
				result['desc_link'] = movie['summary']
				prettyPrinter(result)


		# print(json.dumps(search_result_parsed, indent=4))

def main():
	o = ytsmx()
	what = input()
	o.search(what.replace(' ', '+').strip())

if __name__ == '__main__':
	main()	
