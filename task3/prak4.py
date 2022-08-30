import http.client
from tkinter import *
import re

def maindata():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "06a132a9bbmsh4b2b32d05bbd0d5p1615f3jsn5cc43401ee3c",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    data1=data.decode("utf-8")
    return data1
def getcases(st):
    data1=maindata()
    if data1.find(st)!=-1 and st!='':
        country=re.search(st,data1)
        pochcontr=country.start()
        data=data1[pochcontr:]
        cases=re.search('TotalCases',data)
        poch=cases.start()
        res=''
        allres=''
        s1=True
        i=0
        while s1==True:
            if(data[i+poch]==':'):
                i+=1
                while True:
                    if data[i+poch]==',':
                        s1=False
                        break
                    res+=data[i+poch]
                    i+=1
                    allres=st+' total cases: '+res
            i+=1
        
    else:
        allres='incorrect data' 
    return allres    
def update():
    line1=Label(root,text=getcases('France'), width=30,anchor=W)
    line1.place(x=5,y=5)
    line2=Label(root,text=getcases('Ukraine'), width=30,anchor=W)
    line2.place(x=5,y=25)
    line3=Label(root,text=getcases('UK'), width=30,anchor=W)
    line3.place(x=5,y=45)
    line4=Label(root,text=getcases('Italy'), width=30,anchor=W)
    line4.place(x=5,y=65)
    line5=Label(root,text=getcases('Hungary'), width=30,anchor=W)
    line5.place(x=5,y=85)
    line6=Label(root,text=getcases(str(countryentr.get())), width=30,anchor=W)
    line6.place(x=5,y=125)
root=Tk()
root.title('total cases')
root.geometry('500x500')
line1=Label(root,text=getcases('France'))
line1.place(x=5,y=5)
line2=Label(root,text=getcases('Ukraine'))
line2.place(x=5,y=25)
line3=Label(root,text=getcases('UK'))
line3.place(x=5,y=45)
line4=Label(root,text=getcases('Italy'))
line4.place(x=5,y=65)
line5=Label(root,text=getcases('Hungary'))
line5.place(x=5,y=85)
countryentr=Entry()
countryentr.place(x=5,y=105)
Button(text='update',command= lambda: update()).place(x=400,y=5)


