class Users_C:
  def __init__(self, user_name, initial_investment, ID_num):
    self.user_name = user_name
    self.initial_investment = initial_investment
    self.ID_num = ID_num
    self.cash=initial_investment
    #self.nash=0
    self.port={}
    self.net_worth = initial_investment
    
    
    #return (user_name,initial_investment,ID_num,initial_investment)

  def __str__(self):
    return f"Username: \"{self.user_name}\" | UserID:#{self.ID_num} | Initial Investment Value: ${self.initial_investment} "
