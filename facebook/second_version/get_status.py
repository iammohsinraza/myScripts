import bs4
import urllib.request
import html.parser

quotes = []
print('Enter quotes catagory like: success, funny, love, friendship\n')
keyword = str(input('Enter Catagory: '))
if len(keyword) < 2:
    print('Please Enter Correctly\n')
    keyword = str(input('Enter Catagory Again: s'))
def getQuotes(url,parser):
    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"
        
    opener = AppURLopener()
    response = opener.open(url)
    website = bs4.BeautifulSoup(response,parser)
    for link in website.find_all('a',{'title':'view quote'}):
        quotes.append(link.string)

url = 'https://www.brainyquote.com/search_results.html?q='+keyword
getQuotes(url,'html.parser')

file = open('status.txt','a')
for quote in quotes:
    file.write(quote+'\n*$$*\n')
file.close()
print('Done :D')
