print("Welcome to terminal version of Pyulator.")
print("You can leave the program at any time by pressing 'Ctrl + C' \n")

while quit != 1:
    print("Choose one of the following operations: Addition, Subtraction, Multiplication, Division")
    print()
    selection = str(input()).lower()
    print()
    if (selection == "addition"):
        a, b = input("Input the two numbers you wish to add: ").split()
        print(int(a) + int(b), "\n")
    elif (selection == "subtraction"):
        a, b = input("Input the two numbers you wish to subtract: ").split()
        print(int(a) - int(b), "\n")
    elif (selection == "multiplication"):
        a, b = input("Input the two numbers you wish to multiply: ").split()
        print(int(a) * int(b), "\n")
    elif (selection == "division"): 
        a, b = input("Input the two numbers you wish to divide: ").split()
        if (int(b) == 0):
            print("You can't divide by zero dumbnut...")
            continue
        else:
            print(int(a) / int(b), "\n")
    else: 
        print('Please choose one of the options listed.')

    loop = str(input("Would you like to do another calculation? [Y]/N ")).lower()

    if(loop == "y" or loop == ""):
        continue
    else:
        print("\nThank you for using Pyulator")
        quit = 1