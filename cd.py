import requests
import bs4
import os

MAIN_WEB="https://www.worldometers.info/coronavirus/"
COUNTRY_LIST=['','us','spain','italy','france','germany','turkey','russia','iran','china','brazil','canada','belgium','india','peru','switzerland','portugal','uk','netherlands']


def get_corona_data(web_site,city):
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
    
    if city =="":
        country="world"
    else:
        country=city
    
    country="data\\"+country+"data.csv"
    
    fill_data_to_csv(country,data_listf)

    
    
	
def fill_data_to_csv(country,data_list):

    cases=data_list[0]
    deaths=data_list[1]
    recovered=data_list[2]
    active=cases-(deaths+recovered)
    closed=deaths+recovered
    write_str=str(cases)+","+str(deaths)+","+str(recovered)+","+str(active)+","+str(closed)+"\n"
    file=open(country,'a')
    file.write(write_str)
    file.close()
    
  
def main():
    for city in COUNTRY_LIST:
        if city =="":
            web_site=MAIN_WEB
        else:
            web_site=MAIN_WEB+"country/"+city
        get_corona_data(web_site,city)
 


main()