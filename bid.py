print("Welcome to auction!")
cont = "yes"
bids = {}
while cont=="yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    cont = input("Are there any biders? yes or no?: ").lower()

max = 0
max_person = ""
for name in bids:
    if max<bids[name]:
        max = bids[name]
        max_person = name

print(f"The bid winner is: {max_person}, with the bid of amount: {bids[max_person]}")

