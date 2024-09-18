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
op = input("Enter the operation : ")
num2 = int(input("Enter Number 2 : "))

calculator = operations[op]
answer = calculator(num1,num2)
print(f"{num1} {op} {num2} = {answer}")
    