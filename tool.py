import downloader as dl
from bs4 import BeautifulSoup
import requests
import os
import urllib
from urllib import parse

if (os.path.exists("downloads")):
  print("'/downloads' folder found .")
  os.chdir("downloads")
else :
  print("'/downloads' folder not found")
  print("Creating one ...")
  os.mkdir("downloads")
  os.chdir("downloads")

def get_url_paths(url, ext='', params={}):
  response = requests.get(url, params=params)
  if response.ok:
    response_text = response.text
  else:
    return response.raise_for_status()
  soup = BeautifulSoup(response_text, 'html.parser')
  parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
  return parent


url = input("Directory url : ")
fileformat = input("File Format (Example '.png') : ")
path = parse.urlsplit(url)
ext = '/'
results = get_url_paths(url, ext)

#scans number
snum = 0

for result in results:
	resulturl = result.replace(path.path * 2, path.path); snum += 1
	try:
	  dl.find_file_url(resulturl, fileformat); print("[ SCAN (%s)] [+] Searching for %s files ..." % (snum, fileformat))
	except urllib.error.HTTPError:
		print("[ SCAN ({}) ] Error 404 : no file found .".format(snum))
