#ADD, SHOW, UPDATE, AND DELETE  USER AND THEIR NET_WORTH + ID

#USER HAS TO INPUT THEIR NAME, HOW MUCH MONEY THEY WANT TO ADD IN THEIR ACCOUNT

#WHICH STOCKS TO PURCHASE (LINKING TO THE PORTFOLIO CLASS)
import pickle
import json
from Users import Users_C
from Search_Stocks import search_stock
import requests
import os
import sys

#from Portfolio import Portfolio


class Application:
      
  def __init__(self):
    self.ID=1
    self.userList=[] #list of users (connects with portfolio)


  def add_user(self):

    

    account_name = input(str(f"What is the name of the user? : "))
    # current_users=[]


    # for users in self.userList:
    #   op=self.userList[users]
    #   name= op.user_name
    #   current_users.append(name)
    
    # if account_name in current_users:
    #   print("The username already exists")
    # else:

    ID = self.ID
    invest_amount = float(input("What amount would you like to start investing? : "))
    user_info = Users_C(account_name, invest_amount, ID)
    self.userList.append(user_info)
    print("\nAccount created!\nYour username is \""+ str(account_name) + "\" and your personal user id is \"" + str(ID) + "\"")
    self.ID +=1
    

  

  def update_user(self):
    if self.userList == []:
      print("There are no accounts to update!")
    else:
      acc_id = int(input(f"Please enter the ID of the account to update: "))
      try:
        if int(acc_id)> len(self.userList):
          print("That user does not exist")
        else:
          user_name = str(input("What is the new account username? : "))
          Prin= float(input("What is the new invesment amount in the account? : "))
          self.userList[int(acc_id)-1]=Users_C(user_name,Prin,acc_id)
          return print(f"Your updated username is : \"{user_name}\"")
      except ValueError:
        print("Please enter a valid number!")

  def show_user(self):
    if self.userList == []:
      print("There are no accounts to view!")
    else:
      print("""\n___________________________________________________________________\n
               Current accounts in our stock exchange:
      """)
    for user in self.userList:
      print(user)
      print("""___________________________________________________________________
      """)
    return self.userList
   
  def delete_user(self):
    if self.userList== []:
      print("There are no more accounts to delete!")
    else: 
      user_id = int(input(f"Enter the ID of the user to delete: \n")) ##Add test here
      user_id = user_id - 1
      self.userList.pop(user_id)
      print(f"User Deleted!")
      self.show_user()

  def save(self):
    with open('data.json', 'w') as output_file:
      json.dump(python_data, output_file, indent=4) 

  def quit(self):
    # print("DSDSdS" + self.userList[0])
    list_of_users = str(self.userList)

    print(list_of_users)
    list_of_users=self.show_user()

    choice = input("Would you like to save all changes (y/n): ")
    if choice == 'y' or choice== 'Y':
      self.save(userList)
    sys.exit(0)
    
  def sign_in(self):
    if self.userList== []:
      print("There are no users in the application!")
    else:
      User_ID= int(input("Please enter your user ID to log in: "))
      if User_ID > len(self.userList):
        print('That user ID does not exist!')
      else:
        opened_acc=self.userList[int(User_ID)-1]
        print("Welcome "+ opened_acc.user_name)
      #return(self.inMenu())   
        print("""
        Choose from the options below
        "1": Search stock
        "2": Buy Stock
        "3": Sell Stock
        "4": Check Net Worth
        "5": View Changes
        "6": Return to menu
              """)
        x = int(input("enter: "))

        if x==1:
          self.search_stock()
          return(self.sign_in())
        elif x==2:
          self.buy_stock(opened_acc)
          return(self.sign_in())
        elif x==3:
          self.sell_stock(opened_acc)
          return(self.sign_in())
        elif x ==4:
          self.check_current_net_worth(opened_acc)
          return(self.sign_in())
        elif x == 5:
          self.changes(opened_acc)
          return(self.sign_in())
        else:
          return

       
      
    # app_id = int(input(f"ID of user to update: \n\n"))
    # if int(app_id)> len(self.userList):
    #   print("That user does not exist")
    # else:
    #   app_id - 1
    #   user_to_update = self.userList[int(app_id)]
    #   user_to_update.name = user_name
    #   print("hey ")
    #   print(user_name)

      
        

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
    
    user.current_price =  data["Time Series (5min)"][last_referesh]["1. open"]
    



  def buy_stock(self,user):
    user.initial_investment = user.cash
    print("You currently have $" +str(user.cash)+ " available to spend in your account")
    stock_symbol = input("Please enter the Stock Ticker: ")
    try:
      stock= search_stock(stock_symbol)
    except KeyError:
      print("That stock does not exist. Please enter a valid stock ticker!\n")
      return

      

    stock_price=stock.value
    quant= int(input("\nHow many of this stock would you like to purchase? : "))

            # new_cash= user. = user.cash - (quant*stock_price)

    if (quant*stock_price) > user.cash:
      print('You do not have enough cash to complete your purchase.')
    else:
      user.stock_cost_price = quant*stock_price
      user.nash=user.cash - (quant*stock_price)
      user.cash=user.nash
      user.port[stock_symbol]=[quant,stock_price]
      print('You now have '+ str(quant) + ' share(s) of ' +str(stock_symbol)+ " and $" + str(user.cash)+ " in cash left in your account \n") 
    
    #print(user.port)
    
    #cash= user.invest_investment
    #cash = self.intial_investment
    #print (user.cash)
      #self.search_stock
      #amount_to_buy = int(input("How many stocks do want to buy: "))
      #print("Your updated balance is:")
    

    
  def sell_stock(self, user):
    pass
  #  print(f"you currently have {user.cash} in your account")
  #  print(f"you have {user.stock_cost_price} invested in the market" )

  #  print("do you wish to sell")
  #  x = input(" y or n")

  
  #  if x == "y" or 'Y':
  #    sold_amount = user.cash * st
 


  def check_current_net_worth(self, user):
    print(f"your initial investment was {user.initial_investment}")
    print ( f"you have {user.cash} dollars in your account remaining in ")
    print(f"you have a total of {user.stock_cost_price} invested in the market")
    #  2 of stocks and multiply the value we get from the api
    #   #cash in the account + stocks value
      

  def changes(self, user):
    changes = user.initial_investment - user.initial_investment / user.initial_investment
    print(f"your initial investment was {user.initial_investment}")
    print(f"your change in accouunt balance is: ")
    print (changes)
    # print(float(test) - float(user. = user.cash) /4)
   

    
    
      



# por =  Portfolio_C()
# por.search_stocks



