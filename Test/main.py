import threading
import time
import bs4 as BeautifulSoup
import urllib.request
from urllib.error import URLError,HTTPError
import lxml
import pymysql as ms

## Functions
##
##class Extrator:
##    def __init__(self):
##        self.url = str(input("Please Enter Url Of The Page: "))
##        self.city = str(input("Please Enter City Name: "))
##        self.start = int(input("Start Page: "))
##        self.start = int(input("End Page: "))
##        
##scrapo = Extrator()
conn = ms.connect(host = 'local',user = 'root',password = '',db = 'numbers')
