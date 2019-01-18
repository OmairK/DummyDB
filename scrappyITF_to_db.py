from bs4 import BeautifulSoup
import time
from py2neo import Node,Relationship,PropertyDict,Walkable,Graph,Database
import re



graph= Graph(password='incorrect')

soup = BeautifulSoup(open("/home/daniyal/Desktop/scrapping/itf.html"),"html.parser")
th = soup.find_all('th')

print("HEADINGS")

for i in range (4):
    if th[i].a==True:
        print((th[i].a.text))
    else:
        print(th[i].text)
 




tr = soup.find_all('tr')

    


for i in range(1,251):
    name=re.sub(r'\n\s*\n',r'',tr[i].td.a.text,flags=re.M)
    place=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().text,flags=re.M)
    date=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().text,flags=re.M)
    grade=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().find_next_sibling().text,flags=re.M)
    
    Tournament=Node("Tournament",name=f"{name}",place=f"{place}",date=f"{date}",grade=f"{grade}")
    graph.create(Tournament)




soup = BeautifulSoup(open("/home/daniyal/Desktop/scrapping/itf2.html"),"html.parser")
tr = soup.find_all('tr')




for i in range(1,95):
    name=re.sub(r'\n\s*\n',r'',tr[i].td.a.text,flags=re.M)
    place=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().text,flags=re.M)
    date=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().text,flags=re.M)
    grade=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().find_next_sibling().text,flags=re.M)
    
    Tournament=Node("Tournament",name=f"{name}",place=f"{place}",date=f"{date}",grade=f"{grade}")
    graph.create(Tournament)
    