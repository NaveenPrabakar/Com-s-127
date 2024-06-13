def vegatables(shoppingCart, money):
    carrots = 0.99
    carrot = "carrot"
    lettuce = "lettuce"
    Lettuce = 2.99
    cabbage = "cabbage"
    Cabbage = 2.99
    eggplant1 = "eggplant"
    eggplant = 1.99

    purchase = True

    while purchase == True: 
        veg = input("There are [c]arrots for .99, [L]ettuce for 2.99, and [C]abbage for 2.99, and [e]ggplant for 1.99. or would you like to go to another [a]isle: ")
        
        if veg == "c":
            shoppingCart.append(carrot)
            money.append(carrots)
            print()
            print("You have added carrots to your cart")
            print()
        elif veg == "L":
            shoppingCart.append(lettuce)
            money.append(Lettuce)
            print()
            print("You have added a lettuce to your cart")
            print()
        elif veg == "C":
            shoppingCart.append(cabbage)
            money.append(Cabbage)
            print()
            print("You have added a cabbage to your cart")
            print()
        elif veg == "e":
            shoppingCart.append(eggplant1)
            money.append(eggplant)
            print()
            print("You have added an eggplant to your cart")
            print()
        elif veg == "a":
            break
        else:
            print("Please enter in only the correct vegatbales")
    return shoppingCart, money


def fruits(shoppingCart, money):
    new = True
    apple = 0.99
    Apple = "apple"
    Banana = 0.99
    banana = "banana"
    Orange = 0.99
    orange = "orange"



    while new == True:
        fru = input("There are a[p]ples for .99, [b]ananas for.99, and [o]ranges for .99 or would you like to go to another a[i]sle: ")
        
        if fru == "p":
            shoppingCart.append(Apple)
            money.append(apple)
            print()
            print("You have added an apple to your cart")
            print()
        elif fru == "b":
            shoppingCart.append(banana)
            money.append(Banana)
            print()
            print("You have added a banana to your cart")
            print()
        elif fru == "o":
            shoppingCart.append(orange)
            money.append(Orange)
            print()
            print("You have added an orange to your cart")
            print()

        elif fru == "i":
            new = False
            break
        else:
            print("That item is not on the self")

    
    return shoppingCart, money

def dairy(shoppingCart, money):
    d = True
    Cheese = 0.99
    cheese = "cheese"
    milk = 3.99
    Milk = "milk"
    yogurt = 2.99
    Yogurt = "yogurt"

    while d == True:
        dai = input("There is [c]heese for 0.99, [m]ilk for 3.99, and [y]ogurt for 2.99 or would you like to go to another [a]isle: ")

        if dai == "c":
            shoppingCart.append(cheese)
            money.append(Cheese)
            print()
            print("You have added cheese to your cart")
            print()
        elif dai == "m":
            shoppingCart.append(Milk)
            money.append(milk)
            print()
            print("You have added milk to your cart")
            print()
        elif dai == "y":
            shoppingCart.append(Yogurt)
            money.append(yogurt)
            print()
            print("You have added yogurt to your cart")
            print()
        elif dai == "a":
            break
        else:
            print("Enter a dairy product that is aviable")
    return shoppingCart, money

def meat(shoppingCart, money):
    Steak = 13.99
    steak = "steak"
    Chicken = 8.99
    chicken = "chicken"
    fish = 10.99
    Fish = "fish"
    m = True

    while m == True:
        mea = input("There is [s]teak for 13.99, [c]hicken for 8.99, and [f]ish for 10.99 or back to the [a]isles: ")

        if mea == "s":
            shoppingCart.append(steak)
            money.append(Steak)
            print()
            print("You have added a steak to your carty")
            print()
        elif mea == "c":
            shoppingCart.append(chicken)
            money.append(Chicken)
            print()
            print("You have added a chicken to your cart")
            print()
        elif mea == "f":
            shoppingCart.append(Fish)
            money.append(fish)
            print()
            print("You have added fish to your cart")
            print()
        elif mea == "a":
            break
    return shoppingCart, money

def beverages(shoppingCart, money):
    soda = 4.99
    Soda = "soda"
    apple = 4.99
    Apple = "Apple Juice"
    orange = 4.99
    Orange = "Orange Juice"
    f = True

    while f == True:
        bev = input("There is [s]oda for 4.99, apple [j]uice for 4.99, and [o[range juice for 4.99 or would you like to go back to the [a]isles: ")

        if bev == "s":
            shoppingCart.append(Soda)
            money.append(soda)
            print()
            print("You have added soda to your cart")
            print()
        elif bev == "j":
            shoppingCart.append(Apple)
            money.append(apple)
            print()
            print("You have added apple juice to your cart")
            print()
        elif bev == "o":
            shoppingCart.append(Orange)
            money.append(orange)
            print()
            print("You have added orange juice to your cart")
            print()
        elif bev == "a":
            break
        else:
            print("That is not one of the items on the selves")
    
    return shoppingCart, money

def snacks(shoppingCart, money):
    Chip = 2.99
    chip = "Chips"
    Cookies = 3.99
    cookies = "Cookies"
    candy = 1.99
    Candy = "candy"
    c = True

    while c == True:
        sna = input("There are [c]hips for 2.99, c[o]ookies for 3.99, and c[a]ndy for 1.99, or would you like to go back to the a[i]sles: ")

        if sna == "c":
            shoppingCart.append(chip)
            money.append(Chip)
            print()
            print("You have put a bag of chips in your cart")
            print()
        elif sna == "o":
            shoppingCart.append(cookies)
            money.append(Cookies)
            print()
            print("You have put a bag of cookies into your cart")
            print()
        elif sna == "a":
            shoppingCart.append(Candy)
            money.append(candy)
            print()
            print("You have put a box of candies into your cart")
            print()
        elif sna == "i":
            break
        else:
            print("That item is not in the aile")
    return shoppingCart, money

        

