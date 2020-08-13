import requests
import json
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


def parsing_recommendations(JSON_data):
    recommendation_data = pd.read_json(JSON_data)
    recommendation_data.to_csv('out.csv', index=True)
    df_columns_name = recommendation_data.columns
    df_symbol = recommendation_data['symbol'][0]
    print(df_columns_name)
    print(type(df_symbol))
    #plotting_data(recommendation_data)


def get_recommendation(stock):
    try:
        response = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol=' + stock + '&token=bsok7avrh5r8ktijv08g')
        print('The server has responded with a following status code:', response.status_code)
        response = response.json()
        return response
        
    except requests.exceptions.RequestException as error:
        print('An error has occurred:', error)


def fetching_companies(listOfSymbols):
    arrayOfRecommendations = []
    for symbol in listOfSymbols:
        arrayOfRecommendations += get_recommendation(symbol)
    parsedArray = json.dumps(arrayOfRecommendations)
    parsing_recommendations(parsedArray)

def plotting_data(df):
    print(df)
    sns.boxplot(data=df)
    sns.despine(bottom=True)
    plt.show()
    

#listOfStocks = ['TSM', 'BA', 'AMD', 'SNE']
listOfStocks = ['TSM']

fetching_companies(listOfStocks)