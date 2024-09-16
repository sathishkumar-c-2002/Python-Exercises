smallSize= 15
mediumSize = 20
largeSize = 25

PepperoniForSmall = 2
PepperoniForMedium = 3
xtracheese = 1

size = input("Enter the size of your pizza? S,M,L: ")
addPepperoni = input("Do you want Pepporoni? Y or N:    ")
extraCheese = input("Do you want extra cheese? Y or N:  ")

bill = 0

if size.lower() == "s":
    bill += smallSize
    if addPepperoni.lower() =="y":
        bill += PepperoniForSmall
        if extraCheese.lower() =="y":
            bill+=xtracheese
    
elif size.lower() == "m":
    bill += mediumSize
    if addPepperoni.lower() =="y":
        bill += PepperoniForMedium
        if extraCheese.lower() =="y":
            bill+=xtracheese

elif size.lower() == "l":
    bill += largeSize
    if addPepperoni.lower() =="y":
        bill += PepperoniForMedium
        if extraCheese.lower() =="y":
            bill+=xtracheese
    
    
print(bill)
    