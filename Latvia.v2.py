import choice as choice


def active_kidz():
    name = input("What is your child's name: ")
    age = int(input("What is your child's age: "))
    print("----------------------------------------")
    print()
    print("Your child has been entered into Active Kidz")
    print()
    print("----------------------------------------")
    child_names.append(name)
    child_age.append(age)


def average_age():
    ave_age = sum(child_age) // len(child_age)
    print(ave_age)

child_names = []
child_age = []

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
        active_kidz()

    elif choice == 2:
        input("What is your child's name: ")
        int(input("What is your child's age: "))
        print("----------------------------------------")
        print()
        print("Your child has been entered into Fun In The Sun")
        print()
        print("----------------------------------------")

    elif choice == 3:
        average_age()

    elif choice == 4:
        quit()

    else:
        print("Sorry that is not a valid option")
