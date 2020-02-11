import bs4,requests,webbrowser,os
from bs4 import BeautifulSoup




url='http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print('downloading page %s...' % url)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"html.parser")
    comicelem=soup.select('#comic img')
    if comicelem==[]:
        print('could not find comic image')
    else:
        comicurl='http:'+comicelem[0].get('src')
        #download  image
        print('downloading image %s'%comicurl)
        res=requests.get(comicurl)
        res.raise_for_status()

        #saving image:

        imagefile=open(os.path.join('xkcd',os.path.basename(comicurl)),'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()

    #prev button url:
    prevlink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com' + prevlink.get('href')



print('done!')