import bs4,requests,webbrowser
from bs4 import BeautifulSoup
import re


#mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())



phoneNumRegex = re.compile(r'\d\d\d\d\d\d \d\d\d\d\d')
a="doctors near me phone number"
b=a.split(' ')
print('finding contact details for nearby doctors... ')
res= requests.get('https://google.com/search?q=' + '+'.join(b))
#webbrowser.open('https://google.com/search?q=' + '+'.join(b))
res.raise_for_status()
#print(res.text)

mo = phoneNumRegex.findall(res.text)
for i in range (len(mo)):

    print('\nPhone number found: ' + mo[i])



#trl=open('res.text')
#trsoup=BeautifulSoup(trl.read(), "html.parser")
#trlinkelems=trsoup.select('.r a')
#print(trlinkelems[0])

#soup=BeautifulSoup(res.text, "html.parser")

#linkelems=soup.select('.r a')
#print("length is :",len(linkelems))
#num=min(5,len(linkelems))

#for i in range(10):
    #print('opening result : ', linkelems[i].get('href'))
    #webbrowser.open('http://google.com'+linkelems[i].get('href'))