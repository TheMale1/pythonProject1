import choice as choice


def child_name():
    input("What is your child's name: ")
    input("What program would you like to enter your child into: ")
    child_names.append()

def get_child_age():
     child_age = int(input("What is your child's age: "))



child_names = []

choice == True
while choice:
    print("Welcome to the holiday program enrollemnt")
    print("----------------------------------------")
    print()
    print("1-Active Kidz")
    print("2-Fun In The Sun")
    print("3-Print average age")
    print("4-Exit Site")
    print()
    print("----------------------------------------")
    choice = int(input("Enter a number (1-4): "))

    if choice == 1:
        input("What is your child's name: ")
        int(input("What is your child's age: "))
        print("----------------------------------------")
        print()
        print("Your child has been entered into Active Kidz")
        print()
        print("----------------------------------------")
        

    elif choice == 2:
        input("What is your child's name: ")
        int(input("What is your child's age: "))
        print("----------------------------------------")
        print()
        print("Your child has been entered into Fun In The Sun")
        print()
        print("----------------------------------------")

    elif choice == 3:
        print([])

    elif choice == 4:
        quit()

    else:
        print("Sorry that is not a valid option")
