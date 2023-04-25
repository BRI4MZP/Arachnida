from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
import time

def getexifinfo(filename):
	with Image.open(filename) as image:
		if image.getexif():
			date = {}
			for tag, value in image.getexif().items():
				if tag in TAGS:
					date[TAGS[tag]] = value
			return date
		else:
			return False
if __name__ == "__main__":
	if len(sys.argv) < 2:
		quit("Error: Usage python3 scorpion.py <path>")
	path = sys.argv[1]
	for data in sys.argv[1:]:
		if os.path.exists(data):
			print("File: " + str(data))
			print("Size: " + str(os.path.getsize(data)))
			print("Last modification: " + str(time.ctime(os.path.getmtime(data))))
			print("Last access: " + str(time.ctime(os.path.getatime(data))))
			print("Creation: " + str(time.ctime(os.path.getctime(data))))
			if getexifinfo(data):
				print("EXIF: ")
				for tag, value in getexifinfo(data).items():
					print(str(tag) + ": " + str(value))
			else:
				print("EXIF: False")
		else:
			print("Error: " + str(data) + " not found")
		print("-------------------------------\n")