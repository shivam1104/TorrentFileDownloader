import mechanize
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



'''
for form in br.forms():
    if form.attrs['id'] == 'searchform':
        br.form = form
        break

br.form['k']="Terminator"
a=br.submit()

f=open("TempFile.txt","w")


f1=open("TempFile1.txt","w")
content=a.read()
f1.write(content)

response1=br.response().read()
f.write(response1)
'''


