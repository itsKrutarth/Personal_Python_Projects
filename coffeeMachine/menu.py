class MenuItems:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee,}

                     
class Menu:
    def __init__(self):
        self.menuitems = [
            MenuItems("latte", 2.5, 200, 150, 24),
            MenuItems("espresso", 1.5, 50, 0, 18),
            MenuItems("cappuccino", 3, 250, 50, 24)
        ]
    def getItems(self, item):
        pass
    def find_drink(self, order_name):
        for self.item in self.menuitems:
            if(order_name==order_name):
                return self.item
        return None

