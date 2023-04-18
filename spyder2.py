import argparse
import requests
import os

from bs4 import BeautifulSoup as paco
from urllib.parse import urlparse

# global url, level, rpath
urls, images = set(), set()

def getArgs():
	getter = argparse.ArgumentParser()
	getter.add_argument("URL", help="URL destinada a scrapping", type=str)
	getter.add_argument("-r", action="store_true")
	getter.add_argument("-l", type=int, default=5)
	getter.add_argument("-p", type=str, default="./data/")
	return(getter.parse_args())

# def spyder(url):

# 	#Get the content of url
# 	response = requests.get(url)
# 	htmlresponse = paco(response.text, 'html.parser')
# 	for page in htmlresponse.findAll('a', href=True):
# 		urls.add(page['href'])
# 	# print(urls)
def getUrls(url, level):
	try:
		response = requests.get(url, timeout=5)
		print('hols')
		if response.status_code == 200:
			htmlresponse = paco(response.text, 'html.parser')
			print('eh')
			for x in htmlresponse.findAll('a', href=True):
				if "https" in str(x):
					print(str(x.get("href")) + '\n')
	except Exception:
		print(level, Exception.args)



	print()

if __name__ == "__main__":
	args = getArgs()
	global url, level, rpath, recursive
	url, level, rpath, recursive = args.URL, args.l, args.p, args.r
	getUrls(url, 0)
	# while urls[count]:
	# 	spyder(urls[count])
	# 	count += 1