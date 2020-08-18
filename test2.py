class User:
  def __init__(self,userID,initAmount=0):
    self.userID = userID
    self.balance = initAmount

  def withdraw(self,amount):
    self.balance -= amount

  def deposit(self,amount):
    self.balance += amount

class Party:
  def __init__(self,partyID,users={},order=None):
    self.partyID = partyID
    self.users = {}

    for x in users:
      self.users[x] = users[x]

    self.order = order

  def addOrder(self,order):
    self.order = order

  #sus
  def addUser(self,user):
    self.users.update({user.userID:user})

  def removeUser(self,user):
    self.users.pop(user.userID)


class Order:
  def __init__(self,orderID, party=None):
    self.orderID = orderID
    self.party = party
    self.items = {}

  def addItem(self,item):
    self.items.update({item.itemID:item})

  def removeItem(self,item):
    self.items.pop(item.itemID)

  def calculateTotal(self):
    total = 0
    for x in self.items.values():
      total += x.price
    return total

  def calculateUserCost(self,user):
    total = 0
    for x in self.items.values():
      if user in x.users.values():
        total += x.price/len(x.users)
    return total


class Item:
  def __init__(self,itemID,price,mainUser,users={}):
    self.itemID = itemID
    self.price = price
    self.mainUser = mainUser
    self.users = {} # users

    for x in users:
      self.users[x] = users[x]

    self.users[mainUser.userID] = mainUser
    #self.users.update({mainUser.userID:mainUser})

  def addUser(self,user):
    #print(f"added user {user.userID}")
    self.users[user.userID] = user
    #self.users.update({user.userID:user})

  def removeUser(self,user):
    self.users.pop(user.userID)

  def printInfo(self):
    print(f"ItemID: {self.itemID} ")
    print(f"Price: {self.price} ")
    print(f"mainUser: {self.mainUser} ")
    print(f"users: {self.users} ")

  

