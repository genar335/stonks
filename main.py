import requests
import json
import csv
import pandas as pd

def parsingRecommendations(JSON_data):
    recommendation_data = pd.read_json(JSON_data)
    print(recommendation_data)
    recommendation_data.to_csv('out.csv', index=True)


def getRecommendation(stock):
    try:
        response = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=' + stock + '&token=bsok7avrh5r8ktijv08g')
        print('The server has responded with a following status code:', response.status_code)
        response = response.json()
        print(type(response))
        #response = json.dumps(response)

        return response
        
    except requests.exceptions.RequestException as error:
        print('An error has occurred:', error)


def fetchingCompanies(listOfSymbols):
    arrayOfRecommendations = []
    for symbol in listOfSymbols:
        arrayOfRecommendations += getRecommendation(symbol)
    parsedArray = json.dumps(arrayOfRecommendations)
    print(parsedArray)
    parsingRecommendations(parsedArray)


listOfStocks = ['TSM', 'BA', 'AMD']

fetchingCompanies(listOfStocks)