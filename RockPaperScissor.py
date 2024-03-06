import random

def user_input():
    choice = input("Enter 'rock' , 'paper' or 'scissors': ").lower()
    while choice not in ['rock','paper','scissors']:
        print("INVALID INPUT! Enter your choice between 'Rock','Paper','Scissor'")
        choice = input("Enter a choice between 'rock','paper' or 'scissor'.")
    return choice

def comp_choice():
    comp = random.choice(['rock','paper','scissor'])
    # comp = "rock"
    return comp

def comparison(choice, comp):
    if (choice == comp):
        return "It's a Tie."
    
    elif(choice == "rock" and comp == "scissors") or (choice == "scissors" and comp == "paper") or (choice == "paper" and comp == "rock"):
        return "User Wins."
    
    else:
        return "Computer Wins."

def game():
    choice = user_input()
    comp = comp_choice()
    win = comparison(choice, comp)
    print("You Choose: ", choice)
    print("Comp Choice: ", comp)
    print("Winner: ", win)

game()
