# import requests
# import json
# import os
# from Applications import Application




# class Portfolio_C(Application):
   

#   def search_stock(self):
#     stock_symbol = input("Please enter the Stock Ticker: ")
#     stock_symbol= stock_symbol.upper()
#     base_url  = "https://www.alphavantage.co/query?"
#     key = os.getenv('api_key')
#     query_params = {"function": "TIME_SERIES_INTRADAY" , "symbol": stock_symbol, "interval": "5min", "apikey": key}

#     response = requests.get(base_url, query_params)
#     # response.status_code
#     if response.status_code == 200:
#         print('Success!')
#     elif response.status_code == 404:
#         print('Not Found.')
        
#     #error handling return out of the function



#     data = response.json()

#     last_referesh = data['Meta Data']["3. Last Refreshed"]
#     # print(last_referesh)

#     print (data["Time Series (5min)"][last_referesh]["1. open"])

#     def buy_stock(self):
#       cash = self.initial
#       self.search_stock:
#       in
    

    
#     def sell_stock(self):
#       pass


#     def check_current_net_worth(self):
#       pass
#       #Get #2 of stocks and multiply the value we get from the api
#       #cash in the account + stocks value
      

#     def changes(self):
#       pass
#       # current - initial / initial
      



# por =  Portfolio_C()
# por.search_stocks