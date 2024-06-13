#Naveen Prabakar            #9-28-2022
#Assignment 3

print("Welcome to NIMGRAB!")
print()

print("By: Naveen Prabakar")
print("COM S 127 <section D>")
print()

import random
lowestitems = 4
highestitems = 8
lowesttake = 1
highesttake = 3

gameover = False
currenTurn = 0

while gameover == False:
    choice = input("[p]lay, [i]structions, or [q]uit ")
    if choice == "p":
        number = random.randint(lowestitems, highestitems)
        while number > 0:
            if currenTurn == 0:
                print("It is the Human Turn ", number)
                counter = 0
                while counter == 0:
                    for i in range(0, number):
                        print("|", end= "")
                    print()
                    while True:
                        humaninput = input("Enter an number between (1-3): ")
                        try:
                            humaninput = int(humaninput)
                        except:
                            print("Please enter an integer ")
                            continue
                        if humaninput >= 1 and humaninput <= 3:
                            break
                        else:
                            print("Enter an integer between 1 and 3")
                    print("The Human picks: ", humaninput)
                    number = number - humaninput
                    counter = number
                 
            elif currenTurn == 1:
                print("It is the Computer's Turn: ", number)
                counter = 0
                while counter == 0:
                    for i in range(0, number):
                        print("|", end= "")
                    print()
                    if number > 3:
                        computerinput = random.randint(lowesttake, highesttake)
                        print("The computer chooses:", computerinput)
                    elif number == 3:
                        computerinput = random.randint(1, 2)
                        print("The computer chooses:", computerinput)
                    elif number == 2:
                        computerinput = 1
                        print("The computer chooses:", computerinput)
                    elif number == 1:
                        computerinput = 1
                        print("The computer chooses:", computerinput)
                    number = number - computerinput
                    counter = number
            currenTurn += 1
            currenTurn = currenTurn % 2
        if currenTurn == 0:
            print("The Computer has taken the last item, Therefore the human has won!")
        else:
            print("The human has take the last item, therefore the Computer wins!")
        cureenTurn = 0
    elif choice == "i":
        print("Each player, the human and the computer, take turns remvoing objects from a pool")
        print("Each player can remove between 1 to 3 items ")
        print("The player to take the last item will lose the game")
    elif choice == "q":
        print("Bye, have a great time")
        print("We hope to see you play again")
        print("can't beat the computer? Loser")
        break

