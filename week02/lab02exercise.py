import random
choices = ["Rock", "Paper", "Scissors"]

def main():
    try:
        user_choice = input("Enter your choice: ").capitalize()
        if user_choice not in choices:
            raise ValueError("Invalid choice, enter Rock, Paper, Scissors")
        player_choice = choices.index(user_choice)
        computer_choice = random.randint(0,2)
        print("your choice is:", choices[player_choice])
        print("computer's choice is:", choices[computer_choice])

        if player_choice == computer_choice:
            print("Draw")
        elif ((player_choice == 0 and computer_choice == 2) or
              (player_choice == 1 and computer_choice == 0) or
              (player_choice == 2 and computer_choice == 1)):
            print("You win")
        else:
            print("Computer wins")
    except ValueError as e: print(f"Error: {e}")


if __name__ == "__main__":
    main()