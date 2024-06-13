# Naveen Prabakar   11-11-2022
# Assignment 5

import sys
import pickle

def intiaList():
    todolist = {}
    todolist["Back log"] = []
    todolist["todo"] = []
    todolist["In_Progress"] = []
    todolist["in_review"] = []
    todolist["done"] = []

    return todolist

def savelist(todolist):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todolist, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()
    return todolist

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    return todoList

def checkItem(item, todolist):
    itemFound = False
    keyname = ''
    index = -1
    for keys in todolist:
        if keys == True:
            itemFound = True
            keyname = item
        else:
            keyname = item
            print()
    return itemFound, keyname, 

def additem(item, todolist, tolist):
    x, y = checkItem(item, todolist)
    if x == True:
        print("Error")
    elif x == False:
        print(todolist)
        todolist["Back log"].append(y)

        print()
    return todolist

def deleteitem(item, todolist,):
    print(todolist)
    x, y = checkItem(item, todolist)

    if x == True:
        todolist["Back log"].remove(item)
    
    elif item == False:
        print("Error")
    
    todolist["Back log"].remove(item)
    
    return todolist, item

def moveitem(item, tolist, todolist):

    exput = input("where do you want to move the item ")




    while True:
        if exput == 'todo':
             x, y = deleteitem(item, todolist)
             todolist["todo"].append(y)
             break
        elif exput == 'In_Progress':
             x, y = deleteitem(item, todolist)
             todolist["In_Progress"].append(y)
             break
        elif exput == 'In_Review':
            x, y = deleteitem(item, todolist)
            todolist["in_review"].append(y) 
            break
        elif exput == 'done':
            x, y = deleteitem(item, todolist)
            todolist["done"].append(y)
            break
        else:
            print("Error, it is not one of the lists")
            break


        

    
    return todolist

def printTODOList(todoList):
    for i in todoList:
        print(i, todoList[i])
    
    return None






def runapplication(todolist, toList):
    while True:
        print("-----------------------------------------")
        choice = input("Application Menu: [a]dd to backlog, [m]ove item, [d]elete, [s]ave, [q]uit to main menu ")
        print()

        if choice == 'a':
            item = input("Enter an item: ")
            todolist = additem(item, todolist, toList)
            printTODOList(todolist)

        elif choice == 'm':
            checkItem(item, todolist)

            if len(todolist) == 0:
                print("There are no items to remove")
            elif len(todolist) > 0:
                item = input("Enter an item that you want to move ")
                
                
                if item in todolist["Back log"]:
                     todolist = moveitem(item, toList, todolist)
                     printTODOList(todolist)
                elif item in todolist["todo"]:
                    todolist = moveitem(item, toList, todolist)
                    printTODOList(todolist)
                elif item in todolist["In_Progress"]:
                    todolist = moveitem(item, toList, todolist)
                    printTODOList(todolist)
                elif item in todolist["in_review"]:
                     todolist = moveitem(item, toList, todolist)
                     printTODOList(todolist)
                elif item in todolist["done"]:
                     todolist = moveitem(item, toList, todolist)
                     printTODOList(todolist)
                    


                else:
                    print("error, there is nothing to move in the list or what you are wanting to remove does not exist")
                            
                        
                

            
        
        elif choice == 'd':

            item = input("Enter an item: ")

            if item in todolist["Back log"]:
                deleteitem(item, todolist)
                printTODOList(todolist)
            elif item in todolist["todo"]:
                deleteitem(item, todolist)
                printTODOList(todolist)
            elif item in todolist["In_Progress"]:
                deleteitem(item, todolist)
                printTODOList(todolist)
            elif item in todolist["in_review"]:
                deleteitem(item, todolist)
                printTODOList(todolist)
            elif item in todolist["done"]:
                deleteitem(item, todolist)
                printTODOList(todolist)
            else:
                print("Error, there is nothing to delete there")

            

            


        
        elif choice == 's':
            savelist(todolist)
            print('saving list')
            print()
            printTODOList(todolist)
        
        elif choice == 'q':
            print("Returning to main menu")
            print()
            break
        
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q]. ")
            print()
    
    return todolist







def main():
    taskover = False
    toList = []
    print("Ultimate TodoList")
    print()
    
    print("By Naveen Prabakar")
    print("COM S127 Section D")
    
    print()

    while taskover == False:
        print("-----------------------------------------------------")
        choice = input("Main Menu: [n]ewlist, [l]oadlist, or [q]uit ")
        print()

        if choice == "n":
            todolist = intiaList()
            printTODOList(todolist)
            print(todolist)

            runapplication(todolist, toList)
        
        elif choice == 'l':
            todolist = loadList()

            printTODOList(todolist)

            runapplication(todolist)
        
        elif choice == 'q':
            taskover = True
            print("See ya chump")
        
        else:
            print("Please enter [n], [l], or [q]... ")
            print()

if __name__ == "__main__":
    main()
