import requests
import bs4
import os
import time
from datetime import datetime
import time

MAIN_WEB="https://www.worldometers.info/coronavirus/"


def get_time_data():
    daten=datetime.now()
    dater=daten.strftime("%B %d, %Y")
    timer=daten.strftime("%H:%M:%S")
    list=[dater,timer]
    return list

   
def get_corona_data(web_site,city):
    country=city
    res =requests.get(web_site)
    soup =bs4.BeautifulSoup(res.text,'lxml')
    TotalCases =soup.select('#maincounter-wrap > div > span')
    TotalCoronaCases=TotalCases[0].getText().strip().replace(",","")
    TotalCoronaDeaths=TotalCases[1].getText().strip().replace(",","")
    TotalCoronaRecovered=TotalCases[2].getText().strip().replace(",","")
    data_list=[TotalCoronaCases,TotalCoronaDeaths,TotalCoronaRecovered]
    data_listf=[]
    for data in data_list:
        if data =="N/A":
            data=0
        else:
            data=int(data)
        data_listf.append(data)
        
    data_listf.append(data_listf[0]-(data_listf[1]+data_listf[2]))
    data_listf.append(data_listf[1]+data_listf[2])
    return data_listf

def clear_screen():
    if os.name =="nt":
        os.system('cls')
    else:
        os.system('clear')

def get_website(city):
	if city=="world":
		return MAIN_WEB
	else:
		return (MAIN_WEB+"country/"+city)
    
    

def get_city():
    city=input('Enter the Name of The COUNTRY ------>  ')
    city=city.lower()
    return city
    
def show_data_info(list,country):
    data=list
    dtl=get_time_data()
    clear_screen()
    print("===================================================")
    print("CORONA INFO    COUNTRY ::{}".format(country.upper()))
    print("===================================================")
    print("                              Date ::{}".format(dtl[0]))
    print("                              Time ::{}".format(dtl[1]))
    
    print()
    print("Total Cases  Registered   =  {}".format(data[0]))
    
    print("Total Deaths Registered   =  {}".format(data[1]))
    
    print("Total Recovered Cases     =  {}".format(data[2]))
    
    print("Active Cases              =  {}".format(data[3]))
    print("Closed Cases              =  {}".format(data[4]))
    print("===================================================")
    

def show_data_compare(list1,list2,city1,city2):
    data1=list1
    data2=list2
    dtl=get_time_data()
    clear_screen()
    print("============================================================")
    print("CORONA INFO  +++COMPARING {} and {} ".format(city1.upper(),city2.upper()))
    print("============================================================")
    print("                              Date ::{}".format(dtl[0]))
    print("                              Time ::{}".format(dtl[1]))
    
    print()
    print("                             {}   {}   {} ".format(city1,city2,"Difference","High Risk Country"))
    print("Total Cases  Registered   =  {}   {}   {} ".format(list1[0],list2[0],abs(list1[0]-list2[0])))
    
    print("Total Deaths Registered   =  {}   {}   {} ".format(list1[1],list2[1],abs(list1[1]-list2[1])))
    
    print("Total Recovered Cases     =  {}   {}   {} ".format(list1[2],list2[2],abs(list1[2]-list2[2])))
    
    print("Active Cases              =  {}   {}   {} ".format(list1[3],list2[3],abs(list1[3]-list2[3])))
    print("Closed Cases              =  {}   {}   {} ".format(list1[4],list2[4],abs(list1[4]-list2[4])))
    print("===================================================")
    
    
    
def control_center():
    print("==============================================================")
    print("Choose option from below--->")
    print("1) {:20}               2 {:20}".format("Get a Country Data","Compare Two Countries"))
    print("3) {:20}               4 {:20}".format("Get More Countries Data","Exit"))
    option=input('Enter The Option------->  ')
    if option =='1':
        city=get_city()
        clear_screen()
        print("Getting Info")
        list=get_corona_data(get_website(city),city)
        clear_screen()
        show_data_info(list,city)
    elif option =='2':
        print("**You need to enter '2'  country Names")
        city1=get_city()
        city2=get_city()
        clear_screen()
        print("Getting Info ...")
        list1=get_corona_data(get_website(city1),city1)
        clear_screen()
        print("Comparing ...")
        list2=get_corona_data(get_website(city2),city2)
        show_data_compare(list1,list2,city1,city2)
        
        
        
        
control_center()
