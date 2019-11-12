from bs4 import BeautifulSoup
import os
import requests
def geturl(page):
    url = 'http://www.skinme.cc/skinme/skin/charCore'
    response = requests.post(url,data={'type':1,'pageNumber':page,'orderColunm':'skin_id','orderMode': 'DESC'})
    sp=BeautifulSoup(response.text,'html.parser')
    downurl=[]
    name=[]
    for i in sp.find_all('ul'):
        name.append(i.span.string)
        response1= requests.get(i.a['href'])
        sp1=BeautifulSoup(response1.text,'html.parser')
        downurl.append(sp1.findAll(name="div", attrs={"class" :"char_3d_preview_right"})[0].a['href'])
        print("[+] 添加下载连接成功:"+name[-1])
    return {'downurl':downurl,'name':name}
def downlooad(url,name):
    r=requests.get(url)
    print ("[+] 成功下载"+name)
    path = "./skins/"+name
    a=1
    while os.path.exists(path+".png")==True:
        path = "./skins/"+name+str(a)
        print("[+] 名称重复，名称重定义为"+path+".png")
        a+=1
    with open(path+".png","wb") as f:
        f.write(r.content)
    f.close()
if os.path.exists("skins")==False:
    os.makedirs("skins")
for page in range(3,60):
    m = geturl(page)
    i2=0
    for i in m["downurl"]:
        name = m["name"][i2]
        if name=='':
            name="unknow"
        downlooad(i,name.replace('/',''))
        i2+=1
