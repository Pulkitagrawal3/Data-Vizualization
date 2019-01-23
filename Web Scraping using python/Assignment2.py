#Importing libraries for python
import sys
import importlib
importlib.reload(sys)
import csv
import requests
import ctypes

#Importing beautifulSoup library
from bs4 import BeautifulSoup

#Defining the path and name of the output file
y=':1:US'
outfile=open("./Q1.csv","w")

#defining the header for the csv file
Header="City"+","+"State"+","+"Tempreture"+","+"Phrase"+","+"WindSpeed"+"\n"
outfile.write(Header)

#loop to iterate through the required range
for x in range (1100,1200):
	url='https://weather.com/weather/today/l/USTX' #Defining the webpage from which data needs to be extracted
	url=url+str(x)+y
	response=requests.get(url)
	html=response.content							
	soup=BeautifulSoup((html),"lxml")
	count = 0
	
	#Exception Handling
	if 'error404' in soup:
		ctypes.windll.user32.MessageBoxW(0, "Entry not found", "Alert!", 1)
		break
	else:	
		count += 1
		divs=soup.find('h1',attrs={'classname':'h4 today_nowcard-location'})
		divs=str(divs)
		location=divs[divs.find('classname="h4 today_nowcard-location">')+38:divs.find('<span class="icon icon-font iconset-social icon-share-circle"')]
		
		divs=soup.find('div',attrs={'class':'today_nowcard-temp'})
		divs=str(divs)
		temp=divs[divs.find('classname="today_nowcard-temp">')+48:divs.find('<sup>')]
		
		divs=soup.find('div',attrs={'class':'today_nowcard-phrase'})
		divs=str(divs)
		phrase=divs[divs.find('classname="today_nowcard-phrase">')+35:divs.find('</div>')]
		
		divs=soup.find('div',attrs={'class':'today_nowcard-sidecar component panel'})
		divs=str(divs)
		wind=divs[divs.find('class=""')+10:divs.find('</span>')]
		
		#Writing the required data in the output file
		list_of_cells=location+","+str(temp)+","+phrase+","+wind+"\n"
		outfile.write(list_of_cells)    												
		
		
		#Getting the windspeed in Quitaque
		if 'Quitaque' in location:
			wind_var = wind

#Calculating the average tempreture and writting it in the output file
outfile.write("\n"+"Windspeed in Quitaque is "+","+wind_var+"\n")


