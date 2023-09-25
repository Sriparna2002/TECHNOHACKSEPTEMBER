import random

user_score = 0 
computer_score = 0
tie = 0

print("************* Rock Paper Scissors Game *************")

print()

user_name = input("Enter User Name : ")

print("""
Winning Rulls --------
1. Rock Vs Scissors ---> Rock won
2. Rock Vs Paper ----> Paper won
3. Paper Vs Scissors ---> Scissors won""")

while True:
    print()
    print("""Choices are : 
    1. Rock 
    2. Paper
    3. Scissors """)

    print()

    user_choice = input("Enter Your Choise (Rock, Paper, Scissors): ") 

    if user_choice == "Rock":
        user_choices = "Rock"
    elif user_choice == "Paper":
        user_choices = "Paper"
    else:
        user_choices = "Scissors"

    print("User Choice is : ", user_choices)
    print("Now It's Computer Turn!!")    

    computer= ["rock", "paper", "scissors"]
    computer_choice  = random.choice(computer)

    if computer_choice == "Rock":
        computer_choices = "Rock"
    elif computer_choice == "Paper":
        computer_choices = "Paper"
    else:
        computer_choices = "Scissors"

    print("Computer Choice is : ", computer_choices)

    if (user_choices == "Rock" and computer_choices == "Paper") or (user_choices == "Paper" and computer_choices == "Rock"):
        print("Paper Wins")
        result = "Paper"
    elif (user_choices == "Rock" and computer_choices == "Scissors") or (user_choices== "Scissors" and computer_choices == "Rock"):
        print("Rock Wins")
        result = "Rock"
    elif (user_choices == "Paper" and computer_choices == "Scissors") or (user_choices== "Scissors" and computer_choices == "Paper"):
        print("Scissors Wins")
        result = "Scissors"
    elif (user_choice==computer_choices):
        result = "Tie"
    else:
        print("Condition Fail")

    if result == "Tie":
        print("It's Tie")
        tie += 1
    elif result == user_choices:
        print("User Wins")
        user_score +=1
    else:
        print("Computer Wins")
        computer_score +=1 

    print()
    print("Scores are")
    print(user_name,"'s Score : ", user_score)
    print("Computer Score : ", computer_score)
    print("Tie : ",tie)


    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Thanks for playing!")


