#Multiplication Table Generator with user defined input
n = int(input("Enter the number (tables up to):-  "))
for i in range(1, n+1):
    print(f"\nMultiplication Table for {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j} ")