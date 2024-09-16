totalBill = float(input("Enter your Total Bill: $"))
tipPercentage = int(input("What percentage tip would you like to give? 10 or 12 or 15:  "))
people = int(input("How many people to share:  "))

percentage = (tipPercentage/100)
split = (totalBill/people)*(percentage+1)
print(f"Each person should pay ${round(split,2)}")