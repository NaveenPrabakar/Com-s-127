def delete(shoppingCart, money):
    no = False
    for i in shoppingCart:
        print()
        print(i)
            
    dele = input("Would you like to put someting back from your cart? [y]es or [n]o ")

    if dele == "y":

        x = input("What would you like to put back? ")
        for g in shoppingCart:
            if g == x:
                    no = True
                    
                
        if no == True:
            y = (shoppingCart.index(x))
            shoppingCart.remove(x)
            del money[y]
            print()
            print(x, "has been put back")
            print()
                
        elif no == False:
            print
            print("That item is not in your cart")
            print()
    elif dele == "n":
        print()
    else:
        print("Please enter a yes or no answer")

    
    return shoppingCart, money