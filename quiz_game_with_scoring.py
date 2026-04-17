#Quiz gaming with scoring 
score = 0 
print("Welcome to the Quiz")
print()
print("Here you will be asked 5 questions and options to answer to.")
print()
print("------------------------------------------")
print("First Question")
print("What is the correct file extension for Python files?")
print("A .pt")
print("B .py")
print("C .python")
print("D .pyt")

opt = input("Enter the option:- ")
if opt == "B" or opt =="b":
    print("Yes, it is the correct answer.")
    score+=1
else:
    print("Sorry, it was the wrong option")
print()

print("------------------------------------------")
print("Second Question")
print("Which keyword is used for a loop in Python?")
print("A. repeat")
print("B. loop")
print("C. for")
print("D. iterate")

opt = input("Enter the option:- ")
if opt == "C" or opt =="c":
    print("Yes, it is the correct answer.")
    score+=1
else:
    print("Sorry, it was the wrong option")
print()

print("------------------------------------------")
print("Third Question")
print("Who is known as the father of computers?")
print("A. Alan Turing")
print("B. Charles Babbage")
print("C. Elon Musk")
print("D. Bill Gates")

opt = input("Enter the option:- ")
if opt == "B" or opt =="b":
    print("Yes, it is the correct answer.")
    score+=1
else:
    print("Sorry, it was the wrong option")
print()

print("------------------------------------------")
print("Fourth Question")
print("What is the value of 2³?")
print("A. 5")
print("B. 8")
print("C. 4")
print("D. 9")

opt = input("Enter the option:- ")
if opt == "B" or opt =="b":
    print("Yes, it is the correct answer.")
    score+=1
else:
    print("Sorry, it was the wrong option")
print()

print("------------------------------------------")
print("Fifth Question")
print("Which data type is used to store text in Python?")
print("A. int")
print("B. float")
print("C. str")
print("D. bool")

opt = input("Enter the option:- ")
if opt == "C" or opt =="c":
    print("Yes, it is the correct answer.")
    score+=1
else:
    print("Sorry, it was the wrong option")
print()

if score == 5:
    print("Congrats, You have scored a perfect score, keep it up!!!")
elif score >3:
    print("Excellent, just a couple of errors...")
else:
    print("Never mind, You can always improve, never give up!!")