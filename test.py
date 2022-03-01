item_selling = input("what's the item you are bidding")
reserve_price = int(input("what's your reserve price"))
print(f"The auction of {item_selling} has started")
print("To stop the bidding please enter -1")
Bid = int(input("Please enter a bid: "))
Highest_Bid = 0
while Bid != -1:
    if Bid > Highest_Bid:
        print(f"The highest bid now is ${Bid}")
        Highest_Bid = Bid
    else:
        print("please enter a higher bid")
        print(f"The highest bid is ${Highest_Bid}")
    Bid = int(input("Please enter a bid: "))
if Highest_Bid >= reserve_price:
    print(f"The auction for {item_selling} is finished with a price of {Highest_Bid}")
else:
    print(f"The {item_selling} didn't sell")
