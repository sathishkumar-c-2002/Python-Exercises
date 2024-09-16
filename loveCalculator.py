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
print(f"Your love score is {score}.")


