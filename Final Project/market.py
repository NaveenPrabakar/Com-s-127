#Naveen Prabakar    # 12-5-2022

#Assignment 7       #Section D


import vegtable
import deletefunction
import checkout



def main():

    shopping = True

    shoppingCart = []
    money =  []

    print("Welcome to Shopping simulator")
    print()

    print("By: Naveen Prabakar")
    print("[Com S 127 Section D")


    while shopping == True:
        choice = input("Would you like to [s]hop, look at [d]iscounts, look at the store [m], look at your [c]art, [i]nstructions or [h]ead to checkout ")

        if choice == 's':

            while True:
                aile = (input("Enter which aile you would like to shop "))
                try:
                    aile = int(aile)
                except:
                    print("Please enter an integer: ")
                    print()
                    continue
                if aile <= 6 and aile > 0:
                    break
                else:
                    print()
                    print("Enter a number between ailes 1-6")
                    print()
            

            if aile == 1:
                shoppingCart, money = vegtable.vegatables(shoppingCart, money)

            elif aile == 2:
                shoppingCart, money = vegtable.fruits(shoppingCart, money)
            
            elif aile == 3:
                shoppingCart, money = vegtable.dairy(shoppingCart, money)

            
            elif aile == 4:
                shoppingCart, money = vegtable.meat(shoppingCart, money)
            
            elif aile == 5:
                shoppingCart, money = vegtable.beverages(shoppingCart, money)
            elif aile == 6:
                shoppingCart, money = vegtable.snacks(shoppingCart, money)

                
            
                

        
        elif choice == "m":
            print("Aile 1: Vegtables")
            print("Aile 2: fruits")
            print("Aile 3: Dairy")
            print("Aile 4: Meat")
            print("Aile 5: Beverages")
            print("Aile 6: Snacks")
        
        elif choice == "i":
            print("There are a total of 6 aile")
            print("Each aile has items to purchase and take")
            print("use the 'look at the store[m] option to see what is in each aisle")
            print("after purchasing what items you want, please head to checkout")
        
        
        elif choice == "d":
            print("Discount options: ")
            print("- purchases of 20 dollars or higher will earn you a 5 percent discount")
            print("- purchaes of 40 dollars or higher will result in a 20 percent discount")
            print("-purchaes of 60 dollar or higher will result in a 40 percent discount")
        
        
        elif choice == "c":

            shoppingCart, money = deletefunction.delete(shoppingCart, money)
        
        elif choice == "h":

            total = checkout.discount(money)

            checkout.checkout(shoppingCart, money, total)

            print()

            print("Come back soon")
            
            break
        else:
            print("That is not one of the options")


if __name__ == "__main__":
    main()

