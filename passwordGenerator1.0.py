import random

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "{", "}", "[", "]", ":", ";", "<", ">", ",", "?", "/", "|", "~", "`", ".", ","]

no_letters = int(input("Enter the number of letters:    "))
no_numbers = int(input("Enter the numbers of integers:  "))
no_symbols = int(input("Enter the numbers of symbols:  "))

password = []
for i in range(0,no_letters):
    password.append(random.choice(alphabets))
    
for i in range(0,no_numbers):
    password.append(random.choice(numbers))

for i in range(0,no_symbols):
    password.append(random.choice(symbols))
    
random.shuffle(password)
print(password)