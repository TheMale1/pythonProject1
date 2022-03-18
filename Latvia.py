
def drop_off():
    dog_name = input("What is you dogs name: ")
    time_stayed = input("How many days will your dog stay:")
    dog_names.append(dog_name)
    total_cost = 15.5 * int(time_stayed)
    print("----------------------------------------")
    print()
    print("Thank you for choosing Christchurch Pet Center!")
    print(f"The total cost of your dogs stay will be ${total_cost}")
    print()
    print("----------------------------------------")



def pick_up():
    dog_name = input("What is your dogs name: ")
    time_stayed = input("How long has your dog stayed: ")
    total_cost = 15.5 * int(time_stayed)
    print("----------------------------------------")
    print()
    print("Thank you for choosing Christchurch Pet Center!")
    print(f"The total cost is ${total_cost}")
    print("You can pick up your dog at 3pm")
    print()
    print("----------------------------------------")



def print_roll():
    print(dog_names)


def time_stayed():
    print("How long will your dog stay: ")


def total_cost():
    total_cost = 15.5 * int(time_stayed)


dog_names = []

#main routine
choice = True
while choice:
    print("----------------------------------------")
    print("Welcome to Christchurch Pet Center")
    print("What would you like us to do? Please choose from the list below")
    print("----------------------------------------")
    print()
    print("1 Drop off a dog")
    print("2 Pick up a dog")
    print("3 Print roll")
    print("4 Exit system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        drop_off()
    elif choice == 2:
        pick_up()
    elif choice == 3:
        print_roll()
    elif choice == 4:
        print("Thank you")
        choice = False
    else:
        print("Sorry that is not a valid option")


