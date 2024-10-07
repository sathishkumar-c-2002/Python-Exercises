def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations = {
    "+" : add, "-" : subtract, "*" : multiply, "/": divide
}

num1 = int(input("Enter Number 1 : "))
choice = True
while choice:
    op = input("Enter the operation : ")
    num2 = int(input("Enter Number 2 : "))
    calculator = operations[op]
    answer = calculator(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
    a = input("Do you want to continue Calculation? (Y/N)")
    if a.lower()=="n":
        choice = False
    num1 = answer