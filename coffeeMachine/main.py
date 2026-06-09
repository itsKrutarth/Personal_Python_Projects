from coffee import CoffeeMaker
from menu import Menu, MenuItems

print("Hello!")
print("What would you like?")
coffee = CoffeeMaker()
userInput = input("espresso/latte/cappucino: ")

while(userInput != "off"):
    if(userInput=="report"):
        currentResource = coffee.currentResources()
        for item in currentResource:
            print(f"{item}: {currentResource[item]}")
        #need to add total cash
    
    else:
        coffee.makeCoffee(userInput)

    userInput = input("espresso/latte/cappucino: ")