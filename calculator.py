#Calculator for 2 Numbers
num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))
print("Which operation do you prefer:- A for Addition, S for Subtraction, M for Multiplication, D for Division, E for Exponents")
opt = input()
if opt == "A" or opt =="a":
    print(num1, "+", num2, "=", num1+num2)
elif opt=="S" or opt=="s":
    print(num1, "-", num2, "=", num1-num2)
elif opt=="M" or opt=="m":
    print(num1, "*", num2, "=", num1*num2)
elif opt == "D" or opt=="d": 
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Cannot divide by zero!")
elif opt == "E" or opt=="e":
    print(num1, "raised to", num2, "=", num1 ** num2)
else:
    print("Invalid choice!")
