from bs4 import BeautifulSoup
import requests

url= "https://en.dragon-ball-official.com/"
r=requests.get(url)
print(r.status_code)
if r.ok:
    soup= BeautifulSoup(r.content, 'html.parser')
    print(soup.title)
    print(soup.title.string)
    tags= soup.find_all(class_='tag')
    # collect_info={}
    collect_info=[]
    for tag in tags:
        info = tag.text
        # url= tag.get('href',None)
        # collect_info[url]=info
        collect_info.append(info)
    print(collect_info)