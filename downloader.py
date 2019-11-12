# Packages
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import wget

# finds the files from the url
def find_file_url(url, fileformat):

    url = url.replace(" ","%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))
    for i in x:
        file_name = i.extract().get_text()
        url_new = url + file_name
        url_new = url_new.replace(" ","%20")
        if(file_name[-1]=='/' and file_name[0]!='.'):
             find_file_url(url_new, fileformat)
        if url_new.endswith(fileformat):
          print("Downloading file : ", url_new)
          wget.download(url_new)

# # finds the document files in the url
# def find_text_url(url):

#     url = url.replace(" ","%20")
#     req = Request(url)
#     a = urlopen(req).read()
#     soup = BeautifulSoup(a, 'html.parser')
#     x = (soup.find_all('a'))
#     for i in x:
#         file_name = i.extract().get_text()
#         url_new = url + file_name
#         url_new = url_new.replace(" ","%20")
#         if(file_name[-1]=='/' and file_name[0]!='.'):
#              find_text_url(url_new)
#         if url_new.endswith(".pdf" or ".txt" or ".docx" or ".doc"):
#           print("Downloading file : ", url_new)
#           wget.download(url_new)

# # finds the Data files from the url
# def find_data_url(url):

#     url = url.replace(" ","%20")
#     req = Request(url)
#     a = urlopen(req).read()
#     soup = BeautifulSoup(a, 'html.parser')
#     x = (soup.find_all('a'))
#     for i in x:
#         file_name = i.extract().get_text()
#         url_new = url + file_name
#         url_new = url_new.replace(" ","%20")
#         if(file_name[-1]=='/' and file_name[0]!='.'):
#              find_data_url(url_new)
#         if url_new.endswith(".csv" or ".dat" or ".db" or ".dbf" or ".sav" or ".sql" or ".tar" or ".xml"):
#           print("Downloading file : ", url_new)
#           wget.download(url_new)

# # finds the executable files from the url
# def find_exe_url(url):

#     url = url.replace(" ","%20")
#     req = Request(url)
#     a = urlopen(req).read()
#     soup = BeautifulSoup(a, 'html.parser')
#     x = (soup.find_all('a'))
#     for i in x:
#         file_name = i.extract().get_text()
#         url_new = url + file_name
#         url_new = url_new.replace(" ","%20")
#         if(file_name[-1]=='/' and file_name[0]!='.'):
#              find_exe_url(url_new)
#         if url_new.endswith(".exe" or ".apk" or ".bat" or ".bin" or ".jar" or ".py"):
#           print("Downloading file : ", url_new)
#           wget.download(url_new)

# # finds the video files from a url
# def find_media_url(url):

#     url = url.replace(" ","%20")
#     req = Request(url)
#     a = urlopen(req).read()
#     soup = BeautifulSoup(a, 'html.parser')
#     x = (soup.find_all('a'))
#     for i in x:
#         file_name = i.extract().get_text()
#         url_new = url + file_name
#         url_new = url_new.replace(" ","%20")
#         if(file_name[-1]=='/' and file_name[0]!='.'):
#              find_media_url(url_new)
#         if url_new.endswith(".mp3" or ".mp4" or ".avi" or ".flv" or ".mov" or ".swf"):
#           print("Downloading file : ", url_new)
#           wget.download(url_new)

# def find_compr_url(url):

#     url = url.replace(" ","%20")
#     req = Request(url)
#     a = urlopen(req).read()
#     soup = BeautifulSoup(a, 'html.parser')
#     x = (soup.find_all('a'))
#     for i in x:
#         file_name = i.extract().get_text()
#         url_new = url + file_name
#         url_new = url_new.replace(" ","%20")
#         if(file_name[-1]=='/' and file_name[0]!='.'):
#              find_compr_url(url_new)
#         if url_new.endswith(".zip" or ".rar"):
#           print("Downloading file : ", url_new)
#           wget.download(url_new)
