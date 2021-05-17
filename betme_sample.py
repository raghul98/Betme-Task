import pymongo
from pymongo import MongoClient
import json
import requests

#stores all live and upcoming sports

def main():

#	conn = input("Enter Connection String for DB Connection")
	cluster = MongoClient("mongodb+srv://raghul:raghul98@cluster0.pflrx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#	api_key = input("Enter API Key")
	api_key = '24782dd7f31b2a0ce85f1ad8798d9bbb'
	db = cluster["betting"]
	collection = db["sports"]

	sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
    	'api_key': api_key
	})

	sports_json = json.loads(sports_response.text)
	collection.insert_many(sports_json['data'])
	print("Successfully stored in Sports Collection")
	print("Calling odds request")
	odds_inplay(cluster,api_key)

#odds for live and upcoming matches
def odds_inplay(cluster,api_key):

	db = cluster["betting"]
	collection = db["odds"]
 
	sport_key = 'upcoming'

	odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    	'api_key': api_key,
    	'sport': sport_key,
    	'region': 'uk', # uk | us | eu | au
    	'mkt': 'h2h' # h2h | spreads | totals
	})
	odds_json = json.loads(odds_response.text)

	collection.insert_many(odds_json['data'])

	teams = collection.find('teams')
	odd = collection.find('h2h')
	for team in teams:
		print(team)
	for od in odddd:
		print(od)




if __name__ == "__main__":
    main()
    

