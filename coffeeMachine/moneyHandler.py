class Money:
    def __init__(self):
        self.TotalCash = 0

    def value(self, coin):
        return self.coins[coin]
    
    def calculateRecievedAmount(self, penny, nickle, dime, quarter, cost):
        total = (penny *0.1) + (nickle*0.05)+(dime*0.1) + (quarter*0.25)
        due = total - cost
        if(due==0):
            print("Thanks! Your time will be ready soon!")
            self.TotalCash+=cost
            return True
        if(due>0):
            print(f"Here's you change back of amount: {due}, and your item will be ready soon!")
            self.TotalCash+=cost
            return True
        if(due<0):
            print("Not sufficient amount, please put required amount.")
            return False
        
                

    def currentTotlCash(self):
        return self.TotalCash