# How many days can we live if we ;ive until 90 years old?

age = input("What is your current age:  ")
age = int(age)

yearsRemains = 90 - age
daysRemains = yearsRemains * 365
weeksRemains = yearsRemains * 52
monthsRemains = yearsRemains * 12
 
message = f"You have {daysRemains} days, {weeksRemains} weeks, and {monthsRemains} are left!"
print(message)

