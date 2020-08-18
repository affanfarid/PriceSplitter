import test2

biz1 = test2.Business(50001, 1000)

pyra = test2.User(1,100)
mythra = test2.User(2,100)
pneuma = test2.User(3,100)

goons = [pyra,mythra,pneuma]

party = test2.Party(897)
for x in goons:
  party.addUser(x)

fries = test2.Item(21,5,pyra)
burger = test2.Item(22,10,mythra)
sandwich = test2.Item(23,9,pyra)

#fries.removeUser(mythra)
#fries.printInfo()
#burger.printInfo()

fries.addUser(mythra)

# print("---------")
# fries.printInfo()


order1 = test2.Order(50,party,biz1)

meal = [fries,burger,sandwich]
for x in meal:
  order1.addItem(x)

# print("BEGIN")
# for y in order1.items.values():
#   #print(order1.items.get(y))
#   #order1.items.get(y).printInfo()
#   y.printInfo()
#   print("---------")

#print(order1.calculateTotal())
# print(order1.calculateUserCost(pyra))
# print(order1.calculateUserCost(mythra))


print("BEFORE: ")
biz1.printInfo()
print("=========")
for x in party.users.values():
  x.printInfo()
  print("---------")

order1.payOrder()

print("AFTER: ")
print("=========")
biz1.printInfo()
for x in party.users.values():
  x.printInfo()
  print("---------")








