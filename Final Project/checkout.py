

def discount(money):
    total = 0

    for i in money:
        total += i
    


    if total >= 20 and total < 40:
        print("You meet the requirements for the 1st discount")
        x = total * .05

        total = total - x
        total = round(total, 2)
        x = round(x, 2)
        print("-", x)
    
    elif total >= 40 and total < 60:
        print("You meet the requirments for the 2nd coupon")

        x = total *.2
        

        total = total - x
        total = round(total, 2)
        x = round(x, 2)
        
        print("-", x)
    
    elif total >= 60:
        print("You meet the requirments for the third discount")
        

        x = total *.4
        total = total - x
        total = round(total, 2)
        x = round(x, 2)
        print("-", x)
    else:
        print("You do not meet the requirments for any of the discounts")
    
    
    
    
    return total

def checkout(shoppingCart, money, total):
    tax = total * 0.06
    tax = round(tax, 2)
    total = total + tax
    total = round(total, 2)
    print()
    print("You have proceeded to check out")

    print()

    print("Your total is", total)

    cost = input("[c]ash or C[a]rd: ")

    if cost == "c" or 'a':
        print("Here's your recepit")
        print()
        for i, j in zip(shoppingCart, money):
                print(i,":", j)
                print()

        print("tax: ",tax)
        print("total: ", total)
    else:
        print("Please choose cash or card, stealing is frowned upon")
