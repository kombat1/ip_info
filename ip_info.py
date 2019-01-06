import json
import requests
from bs4 import BeautifulSoup
import argparse

args = argparse.ArgumentParser()
args.add_argument('-i','--ip',help='ip target',metavar='')

group = args.add_mutually_exclusive_group()
group.add_argument('--all',help='all info ip',action="store_true")
group.add_argument('--city',help='city in ip',action="store_true")
group.add_argument('--region',help='region in ip',action="store_true")
group.add_argument('--hostname',help='hostname ip',action="store_true")
group.add_argument('--country',help='country ip',action="store_true")

args = args.parse_args()

def main():
	if args.all:
		all()
	if args.city:
		city()
	if args.region:
		region()
	if args.hostname:
		Hostname()
	if args.country:
		Country()
	
try:
	url = "https://ipinfo.io/" + args.ip + "/json"
except:
	print('Use:python3 ip_info.py --ip 192.168.1.1 --all'); SystemExit

if not args.ip:
	pass 

try:
	getInfo = requests.get(url).text
except:
	print( "\x0a[!] - IP not found! - [!]\x0a" )


def all():


	infoList = json.loads(getInfo)

	try:
		print( "IP: ", infoList["ip"] )
	except:
		print( "IP: ERORR ")
	try:		
		print( "City: ", infoList["city"] )
	except:
		print( "City: ERORR")
	try:		
		print( "Region: ", infoList["region"] )
	except:
		print("Region: ERORR")
	try:		
		print( "Country: ", infoList["country"] )
	except:
		print ("Country: ERORR")	
	try:
		print( "Hostname: ", infoList["hostname"] )
	except:
		print("Hostname: ERORR")

def city ():
	infoList = json.loads(getInfo)

	try:
		print( "IP: ", infoList["ip"] )
	except:
		print( "IP: ERORR ")
	try:		
		print( "City: ", infoList["city"] )
	except:
		print( "City: ERORR")

def region ():
	infoList = json.loads(getInfo)

	try:		
		print( "Region: ", infoList["region"] )
	except:
		print("Region: ERORR")

def Country ():
	infoList = json.loads(getInfo)		

	try:		
		print( "Country: ", infoList["country"] )
	except:
		print ("Country: ERORR")

def Hostname():
	infoList = json.loads(getInfo)

	try:
		print( "Hostname: ", infoList["hostname"] )
	except:
		print("Hostname: ERORR")


try:
	if __name__ == '__main__':
		main()
except:
	pass	