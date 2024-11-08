import random
playing = True
number = str(random.randint(10,20))
print("i will generate a number from 0 to 9, and you have to guess the number  one digit at a time")
print("the game ends when you get one hero!")
while playing:
    guess = input("give me your bet guess! \n")
    if number == guess:
     print("you win the game")
    print("the number was, number")
    break
else:
    print(" your guess isnt quite right, try again.  \n")
while true:
   user_action = input("enter a choice (rock,paper,scissors): ")
   possible_actions = ["rock","paper","scissors"]
   computer_action = random.choice(possible_actions)
   print(f"\nyou chose {user_action}, computer chose {computer_action}.\n")
   if user_action == computer_action:
    print(f"both players selected {user action}.its a tie")
   elif user_action == "rock":
       if computer_action == "scissors":
          print("rock smashes scissors! you win!")
       else:
          print("paper covers rock! you lose!")
   elif user_action == "paper":
       if computer_action == "rock":
          print("paper covers rock! you win!")
       else:
          print("scissor cuts paper! you lose!")
   elif user_action == "scissor":
       if computer_action == "paper":
          print("scissor cuts paper! you win!")
       else:
          print("rock smashes scissors! you lose!")
   play_again = input("play again? (y\n): ")
   if play_again != "y":
      break