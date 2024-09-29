# Menu exercise, now with arrays and loops

#Array full of our grocery items
items = ["Milk", "Bread", "Cheese", "Cereal", "Orange Juice", "Cranberry Juice", "Tomato", "Apple", "Banana"]
#...and their associated costs
costs = [2.00, 3.00, 2.50, 1.40, 1.80, 3.00, 1.25, 1.50, 2.00]

index=0
n=1
for i in items:
    if len(i) < 10:
        print("%d). %s\t\tCOST: %.2f" % (n, i, costs[index]), sep=' ')
    else:
        print("%d). %s\tCOST: %.2f" % (n, i, costs[index]))
    index += 1
    n += 1

cart = []
bill:float = 0
selection:str = ""

while(True):
    selection = input("Which item would you like? ('checkout' to quit)\n> ")
    match selection:
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            cart.append(items[int(selection) - 1])
            bill += costs[int(selection) - 1]
        case "checkout":
            print("You've ordered: \n\t", cart)
            print("Your bill is: %.2f" % (bill))
            break;
        case _:
            print("INVALID CHOICE: %s" % (selection))
