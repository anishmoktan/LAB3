
from Applications import Application
import json
#importing Portfolio class from main

import sys 

imp=Application()
to_Save= imp.userList

class Menu:
 
 def __init__(self):
    self.app = Application()

    self.options = {

      "1": self.app.add_user,

      "2": self.app.update_user,

      "3": self.app.show_user,

      "4": self.app.delete_user,

      "5": self.app.sign_in,

      "Q": self.app.quit

    }
    
 def display_options(self):
    #print out all options to console
      
      print(""" 
            ************* MAIN MENU *************
             Welcome to Last Mile Stock Exchange! 

             Please choose one of the options below:
 
             1. Create an account
 
             2. Update account information(s)
 
             3. View current account(s)

             4. Delete account(s)

             5. Sign in to your account

             Q. Quit

             *************************************
 
             """)


 def run(self):
    while True:
      self.display_options()
      option = input("Enter an option: ")
      action = self.options.get(option)

      if action:
        action()
      else:
        print("{0} is not a valid option, Please try again".format(option))
    

 #def quit(self):
   
  
    # self.app = Application()
    #save_dict= {}
   #list_of_users = self.save.userList
   #print(to_save)

   #choice = input("Would you like to save all changes (y/n): ")
   #if choice == 'y' or choice== 'Y':
     #with open ("list_of_users.txt", "w+") as json_file:
       #json.dump(list_of_users,json_file)
    # print("Your changes have been saved!")

    # else:
    #   print("Your changes will not be saved")
    # sys.exit(0)
    


 