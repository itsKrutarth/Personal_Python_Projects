from menu import Menu
from moneyHandler import Money

class CoffeeMaker:
    
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk":200,
            "coffee": 100,
        }
        self.menu = Menu()
        self.money = Money()

    def hasEnoughResources(self):
        pass

    def currentResources(self):
        return self.resources

    def makeCoffee(self, order_item):
        item = self.menu.find_drink(order_item)
        penny=0
        nickle=0
        dime=0
        quarter = 0

        if (item==None):
            print("no such item found on menu. Please enter right choice.")
        else:
            if(item.ingredients["water"]>self.resources["water"] or 
               item.ingredients["milk"]>self.resources["milk"] or 
               item.ingredients["coffee"]>self.resources["coffee"]):
                print("Not enough resources in the machine. Please refill!")
            else:
                print(f"Amount to be paid: {item.cost}")
                amountGood = False
                while(not amountGood):
                    penny+= int(input("Provide pennies: "))
                    nickle+= int(input("Provide nickle: "))
                    dime+= int(input("Provide dime: "))
                    quarter+= int(input("Provide quarter: "))
                    amountGood = self.money.calculateRecievedAmount(penny, nickle, dime, quarter, item.cost)
                
                if(amountGood):
                    self.resources["water"] -= item.ingredients["water"]
                    self.resources["milk"] -= item.ingredients["milk"]
                    self.resources["coffee"] -= item.ingredients["coffee"]
                    print("Here is your order! Enjoy!")




