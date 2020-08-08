


'''
simulating splitting


'''
class User:
  def __init__(self, userID, firstName,lastName,amount):
    self.userID = userID
    self.firstName = firstName
    self.lastName = lastName
    self.amount = amount

  def withdraw(self,amount):
    self.amount -= amount

  def deposit(self,amount):
    self.amount += amount



class Item:
  def __init__(self, itemID, name, cost, userList):
    self.itemID = itemID
    self.name = name
    self.cost = cost
    self.userList = userList

  def changeCost(self,newCost):
    self.cost = newCost

  def addUser(self, userList):
    for user in userList:
      self.userList.append(user)


class Order:
  def __init__(self, itemDict):
    self.itemDict = itemDict
    self.totalCost = 0
    for item in itemDict:
      self.totalCost += item.cost


  def addItem(self,itemList):
    for item in itemList:
      self.itemDict[item.itemID] = item
      self.totalCost += item.cost



user1 = User(0, "pyra","aegis", 100)
user2 = User(1, "Mythra", "aegis", 100)

item1 = Item(1,"burger", 10, [user1])
item2 = Item(2,"sandwich", 9, [user1])
item3 = Item(3,"fries", 5, [user1])
item3.addUser([user2])

order1 = Order({})
order1.addItem([item1,item2,item3])

print(order1.totalCost)



