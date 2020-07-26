import json
import requests

def search_stock(self):
    stock_symbol = input("Please enter the Stock Ticker: ")
    stock_symbol= stock_symbol.upper()
    base_url  = "https://www.alphavantage.co/query?"
    key = os.getenv('api_key')
    query_params = {"function": "TIME_SERIES_INTRADAY" , "symbol": stock_symbol, "interval": "5min", "apikey": key}

    response = requests.get(base_url, query_params)
    # response.status_code
    if response.status_code == 200:
        print('We were able to find the value of the stock!')
    elif response.status_code == 404:
        print('Sorry we could not find the stock you were looking for')
        return(self.search_stock)
        
    #error handling return out of the function



    data = response.json()

    last_referesh = data['Meta Data']["3. Last Refreshed"]
    # print(last_referesh)
    print("current market price for " + " " + stock_symbol + " "+ " stock is currently")
    print (data["Time Series (5min)"][last_referesh]["1. open"])
    
    return data["Time Series (5min)"][last_referesh]["1. open"]