name1 = input("Enter your name: ")
name2 = input("Enter their name:    ")

fullName = (name1+name2).lower()

t = fullName.count("t") 
r = fullName.count("r")
u = fullName.count("u")
e = fullName.count("e")
true = str(t+r+u+e)

l = fullName.count("l") 
o = fullName.count("o")
v = fullName.count("v")
e = fullName.count("e")
score = str(t+r+u+e) + str(l+o+v+e)

score = int(score)
if score<10 or score>90:
    print(f"Your love score is {score}.You go together like coke and mentos.")
elif score>=40 or score<=50:
    print(f"Your love score is {score}.You already together.")
else:    
    print(f"Your love score is {score}.")


