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
    self.userList=[] #dictionary of accounts (connects with portfolio)
  
  # def from_json(cls, data):
  #       return cls(**data)


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
    user_input = Users_C(account_name, invest_amount, ID)
    self.userList.append(user_input)
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
      if(user_id > len(self.userList)):
        print('Please enter a valid user ID!')
      else:
        user_id = user_id - 1
        self.userList.pop(user_id)
        print(f"User Deleted!")
        self.show_user()

  def save(self,user_List):
    
    # #json_object = json.dumps(user_List)
    # #json_format = list(json_object)
    # print (type(self.userList))
     with open('list_of_users.json', 'w') as output_file:
        
        new =json.dumps(user_List,default=lambda o: o.__dict__, sort_keys=True, indent= 4)
        json.dump(new,output_file)

        # decoded_info= self.from_json(json.loads(new))
        # print(decoded_info)
  def quit(self):
    # print("DSDSdS" + self.userList[0])
    list_of_users = self.userList

    #print(list_of_users)
    #list_of_users=self.show_user()

    choice = input("Would you like to save all changes (y/n): ")
    if choice == 'y' or choice== 'Y':
      self.save(list_of_users)
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
        print("\nWelcome "+ opened_acc.user_name + '!')
      #return(self.inMenu())   
        print("""
        Choose from the options below
        "1": Search stock
        "2": Buy Stock
        "3": Sell Stock
        "4": Check Portfolio
        "5": Return to menu
              """)
        x = int(input("enter: "))

        if x==1:
          self.search_stock(opened_acc)
          return(self.sign_in())
        elif x==2:
          self.buy_stock(opened_acc)
          return(self.sign_in())
        elif x==3:
          self.sell_stock(opened_acc)
          return(self.sign_in())
        elif x ==4:
          self.check_portfolio(opened_acc)
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

      
        

  def search_stock(self,user):
    stock_symbol = input("Please enter the Stock Ticker: ")
    try:
      stock= search_stock(stock_symbol)
    except KeyError:
      print("That stock does not exist. Please enter a valid stock ticker!\n")
      return
 
    
  def buy_stock(self,user):
    #user.initial_investment = user.cash
    print("You currently have $" +str(user.cash)+ " available to spend in your account")
    stock_symbol = input("Please enter the Stock Ticker: ")
    try:
      stock= search_stock(stock_symbol)
    except KeyError:
      print("That stock does not exist. Please enter a valid stock ticker!\n")
      return

    stock_price=stock.value #price got from search_stock class
    quant= int(input("How many of this stock would you like to purchase? : "))

            # new_cash= user. = user.cash - (quant*stock_price)

    if (quant*stock_price) > user.cash:
      print('You do not have enough cash to complete your purchase.')
    else:
      user.cash=user.cash - (quant*stock_price)
      user.port[stock_symbol]=[quant,stock_price] #Stores it to portfolio dictionary
      if quant == 1:
        print('You now have '+ str(quant) + ' share of ' +str(stock_symbol).upper() + " and $" + str(user.cash)+ " in cash left in your account\n")
      else:
        print('You now have '+ str(quant) + ' shares of ' +str(stock_symbol).upper() + " and $" + str(user.cash)+ " in cash left in your account!\n")
       
    
    #print(user.port)
    
    #cash= user.invest_investment
    #cash = self.intial_investment
    #print (user.cash)
      #self.search_stock
      #amount_to_buy = int(input("How many stocks do want to buy: "))
      #print("Your updated balance is:")
    

    
  def sell_stock(self, user):
    print("This is your current portfolio: ")
    for key in user.port:
      if user.port[key][0] > 1:
        print(str(user.port[key][0]) + " shares of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
      else:
        print(str(user.port[key][0]) + " share of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
    stock= input("\nWhich stock would you like to sell? ")
  
    if stock in user.port:
      quant=int(input("How many of those shares would you like to sell? "))
      if quant > user.port[stock][0] or quant <0:
        print("You can only sell" + user.port[stock][0])
      else:
        new= user.port[stock][0] - quant
        user.port[stock][0]= new
        surplus= user.port[stock][1]*quant
        user.cash=user.cash + surplus
        if quant==1:
          print("You have now sold " + str(quant) + " share of " + stock.upper() + " and" + " $" + str(surplus)+ " has been added to your account")
        else:
          print("You have now sold " + str(quant) + " shares of " + stock.upper() + " and" + " $" + str(surplus)+ " has been added to your account")

    else:
      print("You do not own that stock!")
    
   

    
    # if user.port=[]:
    #   print("This account does not have any investment in the portfolio!")
    # else:
    #   print("These are the current stocks in the portfolio")
    #   for stocks in user.port:
    #     print(user)
  #  print(f"you currently have {user.cash} in your account")
  #  print(f"you have {user.stock_cost_price} invested in the market" )

  #  print("do you wish to sell")
  #  x = input(" y or n")

  
  #  if x == "y" or 'Y':
  #    sold_amount = user.cash * st
 


  def check_portfolio(self, user):
    print(f"\nInitial investment ${user.initial_investment}")
    print (f"Current cash in the account: $" + str(round(user.cash, 2)))
    print("________________________________")
    if len(user.port) ==0 :
      print("There are no stock investments currently in the portfolio.\n")
    else:
      print(f"Account's stock portfolio: ")
      for key in user.port:
        if user.port[key][0] > 1:
          print(str(user.port[key][0]) + " shares of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
        else:
          print(str(user.port[key][0]) + " share of " + key.upper() +  " worth " + str(user.port[key][1]) +" each.")
      print('\n')
   
    #  2 of stocks and multiply the value we get from the api
    #   #cash in the account + stocks value
      

  def changes(self, user):
    changes = user.cash - user.initial_investment / user.initial_investment
    print(f"your initial investment was {user.initial_investment}")
    print(f"your change in accouunt balance is: ")
    print (changes)
    # print(float(test) - float(user. = user.cash) /4)
   

    
    
      



# por =  Portfolio_C()
# por.search_stocks



