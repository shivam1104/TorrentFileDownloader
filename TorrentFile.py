import mechanize,os
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



YifyName=raw_input("Enter the movie you wish to download")
String1="https://www.yify-torrent.org/search/"
MovieLink=String1+YifyName+'/'
print MovieLink
br=mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

try:
	pg=br.open(MovieLink)
	content=pg.read()


except:
	print("Check your Internet Connection, or wrong name Entered Cannot Connect to the site")
	sys.exit()

bs=BeautifulSoup(content)
PageSource=open("Page.txt","w")
PageSource.write(bs.prettify().encode('UTF-8'))

print("Found These Movies")

h3s=bs.findAll('h3')

counter=0
for i in h3s:
	counter+=1
	print counter,
	print(i.get_text())
if(counter==0):
	print(" \n Wrong Name or not yet uploaded \n \n ")

print "(Press anything) for Terminating"
Choice=input("\nInput the number of the Movie you wish to download the torrent\n ")

if(Choice>counter):
	print("Terminating...")
	sys.exit()

Choice-=1
text=h3s[Choice].get_text()
text=text.replace('(','')
text=text.replace(')','')
text=text.lower()
print " \n ", text ," \n" 

for a in bs.findAll('a'):
	if ( a.has_attr('href')):
		temphref=a['href'].strip()	
		temphref=temphref.replace('-',' ')
		#print(temphref)
		if( text in temphref):
			print '\n found  url linking.. \n '
			text="https://www.yify-torrent.org"
			text1=text+a['href']
			print(text1)
			textlist=text1.strip().split('/')			
			MovieNumber=textlist[4]
			print(" \n Movie Numer found as "+MovieNumber)
			AlmostLink=text+'/download/torrent-'+MovieNumber+'.html'
			print(AlmostLink)

			#req = br.click_link(text)
			a=br.open(AlmostLink)
			content=a.read()
			bs1=BeautifulSoup(content)

			for b in bs1.findAll('a'):
				if(b.text=="Download Site1"):
					text4="https:"
					FinalTorrent=b['href']
					FinalTorrent=text4+FinalTorrent					
					print(FinalTorrent)

					try:
						TORREENT = br.open_novisit(FinalTorrent)
					except:
						print("File removed from Link 1 Going to Link2")

					filename=YifyName+".torrent"
					with open(filename, 'wb') as f:
						f.write(TORRENT.read())

					print(FinalTorrent)		
					os.system(filename)	
			break



	
