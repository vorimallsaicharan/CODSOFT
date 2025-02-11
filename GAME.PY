import random
def get_user_choice():
    choices = {1: 'paper', 2: 'scissor', 3: 'rock'}
    choice_num = int(input("Enter your choice (1 for paper, 2 for scissor, 3 for rock): "))
    return choices.get(choice_num, "Invalid choice")
def get_computer_choice():
    return random.choice(['paper', 'scissor', 'rock'])
def determine_winner(user_choice, computer_choice):
    outcomes = {
        ('Rock', 'Paper'): "Paper covers  the rock! You lose.",
        ('Rock', 'Scissors'): "Rock smashes the scissors! You win!",
        ('Paper', 'Rock'): "Paper covers the rock! You win!",
        ('Paper', 'Scissors'): "Scissors cuts the paper! You lose.",
        ('Scissors', 'Paper'): "Scissors cuts the paper! You win!",
        ('Scissors', 'Rock'): "Rock smashes the scissors! You lose."
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    return outcomes.get((user_choice, computer_choice), "It's a tie!")
def play_game():
    print("WELCOME TO THE GAME!!!")
    print("\nenter 1 for selecting the Rock \n")
    print("\nenter 2 for selecting the Paper \n")
    print("\nenter 3 for selecting the Scissors\n")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You selected the{user_choice}!")
        print(f"the computer's choice: {computer_choice}\n")
        print("Now it's your Time to Play the game")
        print(determine_winner(user_choice, computer_choice)) 
        if input("Do you want to play the game one more time (Y/N)? ").upper() != 'Y':
            print("Thank you for playing!!")
            break

play_game()