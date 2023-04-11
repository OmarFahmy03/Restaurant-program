#shop cart
cart = []
#calculate total price
price = 0
#contact us function
def Contact_Us():
    print("Phone number : +20 1056831290 \n Address: 52 Riad street-Helwan-Cairo")
    input("Press Enter to continue...")
    start()

#check if user want anything else
def check():
    global price
    choice = input('do you want anything else (y,n) or t for total price \n')
    if choice == 'y':
        Order_Menu()
    elif choice == 't':
            print(price)
    elif choice == 'n':
        return cart

#order menu
def Order_Menu():
    global price
    op2 = int(input("What do you want \n 1: Beef burger \n 2: chicken burger \n 3: additions \n"))
    #beef menu
    if op2 == 1:
        beef = [['beef burger', 2], ['cheese beef burger',3], ['double beef burger', 5]]
        def let_user_pick(beef):
            print("Please choose:")

            for idx, element in enumerate(beef):
                print("{}) {}".format(idx + 1, element))

            i = input("Enter number: ")
            try:
                if 0 < int(i) <= len(beef):
                    return int(i) - 1
                    
            except:
                pass
            return None
        res = let_user_pick(beef)
        #add chosen item to cart
        price = price+beef[res][1]
        cart.append(beef[res][0])
        print(beef[res][0])
        print(cart)
        check()
    elif op2 == 2:
        Chicken = [['Chicken burger', 4], ['cheese Chicken burger',6], ['double Chicken burger', 7]]
        def let_user_pick(Chicken):
            print("Please choose:")

            for idx, element in enumerate(Chicken):
                print("{}) {}".format(idx + 1, element))

            i = input("Enter number: ")
            try:
                if 0 < int(i) <= len(Chicken):
                    return int(i) - 1
                    
            except:
                pass
            return None
        res = let_user_pick(Chicken)
        #add chosen item to cart
        price = price+Chicken[res][1]
        cart.append(Chicken[res][0])
        print(Chicken[res][0])
        print(cart)
        check()
    elif op2 == 3:
        Additions = [['salad', 1], ['cola',8], ['katchup', .5]]
        def let_user_pick(Additions):
            print("Please choose:")

            for idx, element in enumerate(Additions):
                print("{}) {}".format(idx + 1, element))

            i = input("Enter number: ")
            try:
                if 0 < int(i) <= len(Additions):
                    return int(i) - 1
                    
            except:
                pass
            return None
        res = let_user_pick(Additions)
        #add chosen item to cart
        price = price+Additions[res][1]
        cart.append(Additions[res][0])
        print(Additions[res][0])
        print(cart)
        check()
#start menu
def start():
    op = int(input("Please select \n 1: for order \n 2: to contact us \n"))
    if op == 1:
        Order_Menu()
        #print("order")
    elif op == 2:
        Contact_Us()
        #print("contact")
    else:
        print("invalid option")
        start()
start()