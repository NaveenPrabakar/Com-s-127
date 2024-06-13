#Naveen Prabakar               9-24-2022
#Assignment two 


print("Welcome to Magic 9 Ball")
print()

print("By: Naveen Prabakar")
print("[Com S 127 Section D]")
print()

print("What would you like to do?")
choice = input("[c]alculator, [p]rediction, [q]uit: ")

if choice == "c":
    calculation = input("Choose a calculation: [+]. [-], [*], [/], [**]")
    if calculation =="+":
        leftsidenumber = float(input("enter an integer: "))
        rightsidenumber = float(input("Enter an integer: "))
        answer = leftsidenumber + rightsidenumber 
        print("The answer is: ", answer)
    elif calculation == "-":
        leftsidenumber = float(input("enter an integer: "))
        rightsidenumber = float(input("Enter an integer: "))
        answer = leftsidenumber - rightsidenumber
        print("The answer is:  ", answer)
    elif calculation == "*":
        leftsidenumber = float(input("enter an integer: "))
        rightsidenumber = float(input("Enter an integer: "))
        answer = leftsidenumber * rightsidenumber
        print("The answer is: ", answer)
    elif calculation == "/":
        leftsidenumber = float(input("enter an integer: "))
        rightsidenumber = float(input("Enter an integer: "))
        if rightsidenumber == 0:
            print("error, number cannot be 0 on right side")
        else:
            answer = leftsidenumber / rightsidenumber
            print("The answer is: ", answer)
    elif calculation == "%":
        leftsidenumber = float(input("enter an integer: "))
        rightsidenumber = float(input("Enter an integer: "))
        if rightsidenumber == 0:
            print("Error, number cannot be zero on right side")
        else:
            answer = leftsidenumber % rightsidenumber
            print("The answer is: ")
    elif calculation == "**":
        leftsidenumber = float(input("enter an integer: "))
        rightsidenumber = float(input("Enter an integer: "))
        answer = leftsidenumber ** rightsidenumber 
        print("The answer is: ")
elif choice == "p":
    question = input("what is your question? ")
    print("As far as the question is concerned,", question, "I predict: ") 
    length = len(question)
    y = length % 10

    if y == 0:
        print("definitely no")
    if y == 1:
        print("most likely no")
    if y == 2:
        print("no")
    if y == 3:
        print("maybe")
    if y == 4:
        print("I don't know")
    if y == 5:
        print("yes")
    if y == 6:
        print("most likely yes")
    if y  == 7:
        print("definitely yes")
    if y == 8:
        print("Certainly")
    if y == 9:
        print("100 percent")
elif choice == "q":
    print("Bye, have a wonderful rest of your day")
    print("Please use this magic 9 ball soon!")

    


    
