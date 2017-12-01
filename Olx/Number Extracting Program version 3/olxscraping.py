###------IMPORT MODULES------###
import _thread
import urllib.request
import bs4 as BeautifulSoup
import time
###--------------------------###

###------Initializing Values------###

    ###Array to store All page Adds Links###
addsLinks = []
    ##--Array to store All Adds Numbers--###
addsNumber = []

counter = 1;

###---------Location---------###
location = ""
allcities = ""
abbottabad = "abbottabad"
faisalabad="faisalabad"
gujranwala="gujranwala"
gujrat="gujrat"
hyderabad="hyderabad"
islamabad="islamabad"
karachi="karachi"
lahore="lahore"
multan="multan"
peshawar="peshawar"
quetta="quetta"
rawalpindi="rawalpindi"
sargodha="sargodha"
sialkot="sialkot"
  
###--------category----------###
category = ""
allcat = ""
mobiles_tablets = "mobiles-tablets"
electronics_home_appliances="electronics-home-appliances"
vehicles="vehicles"
bikes="bikes"
propertyforsale="property-for-sale"
propertyforrent="property-for-rent"
jobs="jobs"
services="services"
business_industrial_agriculture="business-industrial-agriculture"
furniture_home_decor="furniture-home-decor"
animals="animals"
books_sports_hobbies="books-sports-hobbies"
fashion_beauty="fashion-beauty"
kids_baby_products="kids-baby-products"

###--------------------------###


###-------Source Object------###

def getSourceObject(url,parser):
    source = urllib.request.urlopen(url).read()
    document = BeautifulSoup.BeautifulSoup(source,parser)
    return document

###--------------------------###

###------Fetch Add links-----###
def getAddsLink(url,parser):
    try:
        sourceObject = getSourceObject(url,parser)
        for link in sourceObject.find_all('a',{'class':'marginright5 link linkWithHash detailsLink'}):
            if link:
                addsLinks.append(link['href'])
    except:
        sourceObject = getSourceObject(url,parser)
        for link in sourceObject.find_all('a',{'class':'marginright5 link linkWithHash detailsLink'}):
            if link:
                addsLinks.append(link['href'])
        
            
            

def getCitiesName():
    print("\tAll cities -> 1")
    print("\tabbottabad -> 2")
    print("\tfaisalabad -> 3")
    print("\tgujranwala -> 4")
    print("\tgujrat -> 5")
    print("\thyderabad -> 6")
    print("\tislamabad -> 7")
    print("\tkarachi -> 8")
    print("\tlahore -> 9")
    print("\tmultan -> 10")
    print("\tpeshawar -> 11")
    print("\tquetta -> 12")
    print("\trawalpindi -> 13")
    print("\tsargodha -> 14")
    print("\tsialkot -> 15")

def getCategoryName():
    print("\tAll Category -> 1")
    print("\tMobiles and Tablets -> 2")
    print("\tElectronic and home appliances -> 3")
    print("\tVehicles -> 4")
    print("\tBikes -> 5")
    print("\tProperty for Sale -> 6")
    print("\tProperty for Rent -> 7")
    print("\tJobs -> 8")
    print("\tServices -> 9")
    print("\tBusiness Industrial Agriculture -> 10")
    print("\tFurniture Home Decor -> 11")
    print("\tAnimals -> 12")
    print("\tBooks Sports Hobbies -> 13")
    print("\tFashion Beauty -> 14")
    print("\tKids Baby Products -> 15")
    
            
def getAndSaveAddsnumber(url,parser):
    global counter
    global file_name
    
    getAddsLink(url,parser)
    
    for link in addsLinks:
        
        singleadd = getSourceObject(link,parser).find('strong',{'fnormal'})
        if singleadd:
            
            number = singleadd.string
            file = open(file_name+'.txt','a')
            file.write(number+'\n')
            print(str(counter)+' '+number+':Saved')
            counter += 1
        else:
            print('This Page has no number.')
        
        
def sayWelcome():
    print("###-----Scrapo by Mohsin Raza-----###")
    print('Please Select A City Number Form Where You Want To Extract Numbers.\n\n')
    
    

def getLocation(number):
    global location
    if(number == 1):
        location = allcities
    elif(number == 2):
        location = abbottabad
    elif(number == 3):
        location = faisalabad
    elif(number == 4):
        location = gujranwala
    elif(number == 5):
        location = gujrat
    elif(number == 6):
        location = hyderabad
    elif(number == 7):
        location = islamabad
    elif(number == 8):
        location = karachi
    elif(number == 9):
        location = lahore
    elif(number == 10):
        location = multan
    elif(number == 11):
        location = peshawar
    elif(number == 12):
        location = quetta
    elif(number == 13):
        location = rawalpindi
    elif(number == 14):
        location = sargodha
    elif(number == 15):
        location = sialkot
    else:
        print('Please enter a number correctly')
        exit()

def getCategory(number):
    global category
    if(number == 1):
        category = allcat
    elif(number == 2):
        category = mobiles_tablets
    elif(number == 3):
        category = electronics_home_appliances
    elif(number == 4):
        category = vehicles
    elif(number == 5):
        category = bikes
    elif(number == 6):
        category = propertyforsale
    elif(number == 7):
        category = propertyforrent
    elif(number == 8):
        category = jobs
    elif(number == 9):
        category = services
    elif(number == 10):
        category = business_industrial_agriculture
    elif(number == 11):
        category = furniture_home_decor
    elif(number == 12):
        category = animals
    elif(number == 13):
        category = books_sports_hobbies
    elif(number == 14):
        category = fashion_beauty
    elif(number == 15):
        category = kids_baby_products
    else:
        print('Please enter a number correctly')
        exit()
###-----Validating variables------##
parser = 'html.parser'

sayWelcome()
getCitiesName()
try:
    getLocation(int(input("\n\n\tFrom 1 to 15: ")))
except:
    print('\n\n\tPlease enter again number Correctly')
    getLocation(int(input("\n\n\tFrom 1 to 15: ")))
print('\n\n\n')
getCategoryName()
try:
    getCategory(int(input("\n\n\tFrom 1 to 15: ")))
except:
    print('\n\n\tPlease enter again number Correctly')
    getLocation(int(input("\n\n\tFrom 1 to 15: ")))
    
print('\n\n\n')
file_name = input("\tName the file: ")
print('\n\n\n')

if len(location)==0 and len(category)==0:
    url = 'https://www.olx.com.pk/all-results/'
    print(url)
if len(location) > 0 and len(category) == 0:
    url = 'https://www.olx.com.pk/'+location+'/'
    print(url)
if len(location) < 1 and len(category) > 0:
    url = 'https://www.olx.com.pk/'+category+'/'
    print(url)
if len(location) > 0 and len(category) > 0:
    url = 'https://www.olx.com.pk/'+location+'/'+category+'/'
    print(url)

multiple_time = str(input('Do you want to Extract Multiple Pages numbers?(yes/no) : '))

if multiple_time.lower() == 'yes':
    print('the program run from last save state')
    page_end = int(input('end on Page number: '))
    newFile = open('config.txt','r')
    data = newFile.readlines()
    page_start = int(data[0])
    newFile.close()
    if page_end <= page_start:
        print('last page Number should be greater then Start Page number.Please Run program again ')

    else:
        for session in range(page_start,page_end+1):
           
            addsLinks = []
            addsNumber = []
            ender_url = '?page='+str(session)
            full_url = url+ender_url
            print ('Extracting Number From this Url ('+full_url+')')
            ##getAndSaveAddsnumber(full_url,parser)
            _thread.start_new_thread(getAndSaveAddsnumber(full_url,parser))
            _thread.start_new_thread(getAndSaveAddsnumber(full_url,parser))
            _thread.start_new_thread(getAndSaveAddsnumber(full_url,parser))
            _thread.start_new_thread(getAndSaveAddsnumber(full_url,parser))
            
            writeFile = open('config.txt','w')
            a_incre = session+1
            writeFile.write(str(a_incre))
            writeFile.close()
          
      
else:
    getAddsLink(url,parser)
    getAndSaveAddsnumber(parser)
    print('Done')

