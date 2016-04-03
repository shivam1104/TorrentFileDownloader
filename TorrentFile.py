import mechanize
YifyName=raw_input("Enter the movie you wish to download")
br=mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

try:
	pg=br.open('https://www.yify-torrent.org/search/1080p/')

except:
	print("Check your Internet Connection, Cannot Connect to the site")


for form in br.forms():
    if form.attrs['id'] == 'searchform':
        br.form = form
        break

br.form['k']=YifyName
br.submit()

f=open("TempFile.txt","w")

response1=br.response().read()
f.write(response1)



