import re
import time
import os

from bs4 import BeautifulSoup
from py2neo import Node,Relationship,PropertyDict,Walkable,Graph,Database

dir = os.getcwd()
print(dir)

graph= Graph(password='incorrect')

soup = BeautifulSoup(open("{}/itf.html".format(dir)),"html.parser")
th = soup.find_all('th')

print("HEADINGS")

for i in range (4):
    if th[i].a==True:
        print((th[i].a.text))
    else:
        print(th[i].text)





tr = soup.find_all('tr')




for i in range(1,251):
    """
        Range is specific to the number of events on the first page of ITF website

    """
    name=re.sub(r'\n\s*\n',r'',tr[i].td.a.text,flags=re.M)
    place=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().text,flags=re.M)
    date=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().text,flags=re.M)
    grade=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().find_next_sibling().text,flags=re.M)

    Tournament=Node("Tournament",name="{}".format(name),place="{}".format(place),date="{}".format(date),grade="{}".format(grade))
    graph.create(Tournament)




soup = BeautifulSoup(open("{}/itf2.html".format(dir)),"html.parser")
tr = soup.find_all('tr')




for i in range(1,95):
    """
        Range is specific to the number of events on the second page of ITF website

    """
    name=re.sub(r'\n\s*\n',r'',tr[i].td.a.text,flags=re.M)
    place=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().text,flags=re.M)
    date=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().text,flags=re.M)
    grade=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().find_next_sibling().text,flags=re.M)

    Tournament=Node("Tournament",name="{}".format(name),place="{}".format(place),date="{}".format(date),grade="{}".format(grade))
    graph.create(Tournament)

