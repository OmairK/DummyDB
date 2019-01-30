import re
import time
import os
import pprint

from bs4 import BeautifulSoup
from pymongo import MongoClient

dir = os.getcwd()

client = MongoClient('mongodb://localhost:27017') #port 27017
# db = client.torna_database

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
    
    startDate,endDate = date.split("-")
    startDateDay,startDateMonth = startDate.split()
    endDateDay,endDateMonth,Year = endDate.split()

    
    Tournament = {"name": "{}".format(name),
                  "place": "{}".format(place),
                  "date": "{}".format(date),
                  "start date": [{
                      "day": "{}".format(startDateDay),
                      "month": "{}".format(startDateMonth)}],
                  
                  "end date": "{}".format(endDate),
                  
                  "start date": [{
                      "day": "{}".format(endDateDay),
                      "month": "{}".format(endDateMonth)}],
                  "year": "{}".format(Year),
                
                  
                  "grade": "{}".format(grade)}
    posts = db.posts
    post_id = posts.insert_one(Tournament).inserted_id

        
    





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
    
    startDate,endDate = date.split("-")
    startDateDay,startDateMonth = startDate.split()
    endDateDay,endDateMonth,Year = endDate.split()

    
    Tournament = {"name": "{}".format(name),
                  "place": "{}".format(place),
                  "date": "{}".format(date),
                  "start date": [{
                      "day": "{}".format(startDateDay),
                      "month": "{}".format(startDateMonth)}],
                  
                  "end date": "{}".format(endDate),
                  
                  "start date": [{
                      "day": "{}".format(endDateDay),
                      "month": "{}".format(endDateMonth)}],
                  "year": "{}".format(Year),
                
                  
                  "grade": "{}".format(grade)}
    
    

db.collection_names(include_system_collections=False)
for post in posts.find():

    pprint.pprint(post)