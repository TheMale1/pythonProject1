import random

def game_number():
    game_count = 0
    game_count += 1

while game_count <= 3:
    user_action = input("Choose an option (Rock, Paper, Scissors): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choose {user_action}, the computer chose {computer_action}.\n")

    if user_action == computer_action:
        print("Its a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
         print("Rock smashes Scissors. You win!")
    else:
        print("Paper covers Rock. You lose!")

    if user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock. You win!")
        else:
            print("Scissors cut Paper. You lose!")

    if user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper. You win!")
    else:
        print("Rock smashes Scissors. You lose!")


