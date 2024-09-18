
bid = {}

bidderChoice = False


def winnerName(bid):
    highAmount = 0
    winner = ""
    for key in bid:
        if bid[key]>highAmount:
            highAmount = bid[key]
            winner = key
    print(f"The winner is {winner}  with the bid of ${highAmount}.")
        
            
while not bidderChoice:
    name = input("Enter the Bidder name: ")
    price = int(input("Enter the Bid Amount: $"))
    
    bid[name] = price
    
    nextTime = input("Is any other Bidder is rise? Y or N:  ")
    if nextTime.lower()=="n":
        bidderChoice = True
        winnerName(bid)



    




