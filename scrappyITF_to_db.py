import re
import time
import os

from bs4 import BeautifulSoup
from pymongo import MongoClient

dir = os.getcwd()

client = MongoClient('mongodb://localhost:27017') #port 27017
db = client.torna_database
print(db)
soup = BeautifulSoup(open("{}/itf.html".format(dir)),"html.parser")
th = soup.find_all('th')


for i in range (4):
    if th[i].a==True:
        print((th[i].a.text))
    else:
        print(th[i].text)



db = client.test_database
collection = db.test_database
tr = soup.find_all('tr')




for i in range(1,251):
    """
        Range is specific to the number of events on the first page of ITF website

    """
    name=re.sub(r'\n\s*\n',r'',tr[i].td.a.text,flags=re.M)
    place=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().text,flags=re.M)
    date=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().text,flags=re.M)
    grade=re.sub(r'\n*\n',r'',tr[i].td.find_next_sibling().find_next_sibling().find_next_sibling().text,flags=re.M)
    Tournament = {"name": "{}".format(name),
                  "place": "{}".format(place),
                  "date": date,
                  "grade": "{}".format(grade)}
    posts = db.posts
    post_id = posts.insert_one(Tournament).inserted_id

        
    # DATE=Node("DATE",date="{}".format(date))
    # GRADE=Node("GRADE",grade="{}".format(grade))
    # PLACE=Node("PLACE",place="{}".format(place))

    # date_search = list(graph.find("DATE", property_key ='date',property_value = date))
    # grade_search = list(graph.find("GRADE", property_key ='grade',property_value = grade))
    # place_search = list(graph.find("PLACE", property_key ='place',property_value = place))
    # if len(date_search) > 0:
    #     DATE = matcher.match("DATE",date="{}".format(date))
    # else:
    #     graph.create(DATE)

    # if len(grade_search) > 0:
    #     GRADE = matcher.match("GRADE",grade="{}".format(grade))

    # else:
    #     graph.create(GRADE)


    # if len(place_search) > 0:
    #     PLACE = matcher.match("PLACE",place="{}".format(place))

    # else:
    #     graph.create(PLACE)

    # TOURNAMENT = Node("TOURNAMENT",tourna = "{}".format(name))
    # TOURNAMENT_date = Relationship(TOURNAMENT,"is on",DATE)
    # TOURNAMENT_place = Relationship(TOURNAMENT,"is at",PLACE)
    # TOURNAMENT_grade = Relationship(TOURNAMENT,"is of grade",GRADE)





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
    
    Tournament = {"name": "{}".format(name),
                  "place": "{}".format(place),
                  "date": date,
                  "grade": "{}".format(grade)}
    posts = db.posts
    post_id = posts.insert_one(Tournament).inserted_id
    
    # Tournament=Node("Tournament",name="{}".format(name),place="{}".format(place),date="{}".format(date),grade="{}".format(grade))
    # graph.create(Tournament)

db.collection_names(include_system_collections=False)