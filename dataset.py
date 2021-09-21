import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films'
req=requests.get(url)

soup=bs(req.content)
results=soup.select(".wikitable.sortable tr")

base_add='https://en.m.wikipedia.org'

def more_details(data_three):
    url_test=data_three
    req_test=requests.get(url_test)
    soup_test=bs(req_test.content)
    info_box=soup_test.find(class_='infobox vevent')
    info_rows=info_box.find_all('tr')
    def get_content_value(row_data):
        if row_data.find('li'):
            return [li.get_text(" ",strip=True).replace('\xa0'," ") for li in row_data.find_all('li')]
        else:
            return row_data.get_text(" ",strip=True).replace('\xa0'," ")
        
    movie_info={}
    for idx,row in enumerate(info_rows):
        if idx == 0:
            movie_info['Title']=row.find('th').get_text(" ",strip=True).replace('\xa0'," ") 
        elif idx == 1:
            continue
        else:
            content_key=row.find('th').get_text(" ",strip=True).replace('\xa0'," ") 
            for j in row.find_all(['sup','span']):
                    j.decompose()
            content_value=get_content_value(row.find('td'))
            movie_info[content_key]=content_value
        
    return movie_info

lists=[]

for index,value in enumerate(results):
    
    if index == 0:
        continue
    else:
        try:
            print("Movie Name : ",value.i.get_text())
            data_one=value.i.get_text()
            date_find=value.find_all('td')
            print("Movie release date : ",date_find[2].get_text())
            data_two=date_find[2].get_text()
            for j in value.find_all('sup'):
                j.decompose()
            
            data_three=base_add+value.i.a['href']
            print("Wikipedia link : ",data_three)
            data_four=more_details(data_three)
            print("Running Time : ",data_four['Running time'])
            print("Budget",data_four['Budget'])
            print("Box office",data_four['Box office'])
            print("*"*100)
            
            lists.append([data_one,data_two,data_three,data_four['Running time'],data_four['Budget'],data_four['Box office']])
        except Exception as e:
            continue
           

new_lists=[]
for i in range(len(lists)):
    y=lists[i][1].replace('\n',"")
    if y=='':
        y=y.replace('',"N/A")
    
    x=lists[i][0]
    z=lists[i][2]
    p=lists[i][3]
    q=lists[i][4]
    r=lists[i][5]
    new_lists.append([x,y,z,p,q,r])
df = pd.DataFrame(new_lists, columns = ['Movie_name', 'Movie_release_date','Wikipedia_link','Running_time','Budget','Box_office'])
df.to_csv('Disney_movies.csv')