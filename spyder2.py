import argparse
import requests
import os
from bs4 import BeautifulSoup as paco

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
# def maker(actually, next):
#     actually = urlparse(actually)
#     next = urlparse(next)
#     protocolo, dominio, path, params = next.scheme, next.netloc, next.path, next.params
#     if protocolo == '':
#         protocolo = actually.scheme
#     if dominio == '':
#         dominio = actually.netloc
#     if path == '':
#         path = actually.path
#     if params == '':
#         params = actually.params
#     adv = protocolo + '://' + dominio + path + params
#     return str(adv)

def verifyer(picture):
	tags = ["jpg", "jpeg", "png", "gif", "bmp", "docx", "pdf"]
	for tag in tags:
		if picture.endswith(tag):
			return(True)
	return(False)

def getImages():
	for x in urls:
		try:
			response = requests.get(x, timeout=5)
			htmlresponse = paco(response.text, 'html.parser')
			allimages = htmlresponse.find_all('img')
			for picture in allimages:
				changer = picture.get('src')
				if verifyer(changer):
					images.add(changer)
				continue
		except Exception:
			pass
def download():
	count = 0
	for imagen in images:
		try:
			data = requests.get(imagen, timeout=5)
			if data.status_code == 200:
				if not os.path.exists(rpath):
					os.mkdir(rpath)
				name = imagen.split("."[-1])
				with open(rpath + '/' + str(count) + '.' + name[-1], "wb") as creator:
					creator.write(data.content)
					count += 1
		except:
			pass
def local():


def getUrls(url, lv):
	try:
		response = requests.get(url, timeout=5)
		if response.status_code == 200:
			htmlresponse = paco(response.text, 'html.parser')
			for x in htmlresponse.findAll('a', href=True):
				url = str(x['href'])
				if url not in urls and url.startswith("http://") or url.startswith("https://"):
					urls.add(url)
					# print(url)
					# print(url)
					# print(level)
					# print("lv: " + str(lv) + "level: "+ str(level))
					if int(lv) < int(level):
						# print("lv: " + str(lv) + "level: "+ str(level))
						getUrls(url, int(lv) + 1)
	except Exception:
		pass

if __name__ == "__main__":
	args = getArgs()
	global url, level, rpath, recursive
	url, level, rpath, recursive = args.URL, args.l, args.p, args.r
	try:
		open(rpath, 'r')
	except:
		if args.l != 0:
			getUrls(url, 0)
		else:
			urls.add(url)
	print("HOLA")
	getImages()
	print("aroo")
	download()
	# print (images)
	# print(urls)
	# print(len(urls))
	# while urls[count]:
	# 	spyder(urls[count])
	# 	count += 1