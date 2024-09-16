m = float(input("enter the height:    "))
kg = float(input("Enter the weight in kg:   "))

result = kg/(m*m)
if result<18.5:
    print(f"Your Weight is {result} and You're Underweight")
if result<25:
    print(f"Your Weight is {result} and You're Normal Weight")
if result<30:
    print(f"Your Weight is {result} and You're Overweight")
if result<35:
    print(f"Your Weight is {result} and You're Obese")
else:
    print(f"Your Weight is {result} and You're Clinically Obese")        