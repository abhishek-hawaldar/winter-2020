import bs4,requests,webbrowser
from bs4 import BeautifulSoup




a=input("ENTER THE TERM YOU WANT TO SEARCH:")
b=a.split(' ')
print('googling....')
res= requests.get('https://google.com/search?q=' + '+'.join(b))
res.raise_for_status()
print(res.text)


trl=open('htmlpage.html')
trsoup=BeautifulSoup(trl.read(), "html.parser")
trlinkelems=trsoup.select('.r a')
print(trlinkelems[0])

soup=BeautifulSoup(res.text, "html.parser")

linkelems=soup.select('.r a')
print("length is :",len(linkelems))
num=min(5,len(linkelems))

for i in range(10):
    print('opening result : ', linkelems[i].get('href'))
    webbrowser.open('http://google.com'+linkelems[i].get('href'))