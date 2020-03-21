from bs4 import BeautifulSoup
import requests

# Below is the Indian Government Website
url="https://www.mohfw.gov.in/"
r= requests.get(url)
#soup currently contains the complete html code
soup=BeautifulSoup(r.content,"html.parser")
#temp contains all the "td" tags
temp=soup.find_all("td")

#This loop shows them in text format
for i in range(len(temp)):
    print(temp[i].text)
#empty Dictionary so that now we can add the data in it
dict={}
# this loops add the data in the Dictionary
try:
    for i in range(1,len(temp),6):
        dict.update({temp[i].text: [temp[i+1].text,temp[i+2].text,temp[i+3].text,temp[i+4].text]})
except IndexError as error:
    print("happens ")
#to view the whole data
state_name=input("Enter the complete name of the state \n")
ans=dict.get(state_name)
print("total Confirmed cases are", ans[0])
print("total confirmed Cases are ", ans[1])
print("Cured/Discharged/Migrated", ans[2])
print("deaths occured " ,ans[3])
