###------IMPORT MODULES------###

import urllib.request
import bs4 as BeautifulSoup
import time
from socket import *

###--------------------------###


file =  open('config.txt','r')
line = file.readlines()


start = line[1].split('>')
start = start[1].strip()

end = line[2].split('>')
end = end[1].strip()

saveFile = line[3].split('>')
saveFile = saveFile[1].strip()

url = line[0].split('>')
url = url[1].strip()
file.close()
counter = 1
for session in range(int(start),int(end)+1):
    print('somthing')
    
    completeUrl = url+'?page='+str(session)
    print(completeUrl)
    
    try:
        source = urllib.request.urlopen(completeUrl, timeout=10).read()
    except (UnicodeDecodeError, socket.timeout, urllib.error.URLError):
        continue
    document = BeautifulSoup.BeautifulSoup(source,'html.parser')
    an_file = open(saveFile,'a')
    for single in document.find_all("span", { "class" : "generic-green" }):
            number = single.string
            an_file.write(number+'\n')
            print(str(counter)+' ===== '+ number)
            counter+=1
    
    last_page = str(session)
    file = open('config.txt','w')
    mohsin = session + 1
    line[1] = 'start======>'+str(mohsin)+'\n'
    for single_line in line:
        file.write(single_line)
    file.close()
    an_file.close()
file.close()            
print('Complete')


