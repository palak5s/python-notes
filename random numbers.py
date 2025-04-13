import random
# print(help(random))
# low = 1
# high = 100
# numbers = random.randint(1,6)
# numbers = random.randint(low,high )
# numbers = random.random()
# print(numbers)
# options = ("rock","paper","scissors")
# option = random.choice(options)
# card = ["2","3","4","5","6","7","8","9","10","J","Q","k","A"]
# random.shuffle(card)
# print(card)
######################################## PYTHON NUMBER GUESSING GAME
# import random
# lowest_num =1
# highest_num = 100
# answer = random.randint(lowest_num,highest_num)
# guesses = 0
# is_running = True
# print("Python Number Guessing Game ")
# print(f"Select a number between {lowest_num} and {highest_num}")
# while is_running:
#     guess = input("Enter your guess:")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("number is our of range")
#             print(f"Select a number between {lowest_num} and {highest_num}")
#         elif guess<answer:
#             print("too low")
#         elif guess>answer:
#             print("too high")
#     else:
#         print("invalid guess")
#         print(f"Select a number between {lowest_num} and {highest_num}")
################################### Rock,Paper, Scissors
# import random
# options =("rock","paper","scissor")
#
# running = True
#
# while  running:
#       player = None
#       computer = random.choice(options)
#       while player not in options:
#         player = input("enter a choice (rock,paper,scissor): ")
#         print(f"palyer:{player}")
#         print(f"computer:{computer}")
#       if player == computer:
#                print("it's a tie!")
#       elif player == "rock" and computer =="scissor" :
#         print("player wins")
#       elif player == "scissor" and computer == "paper" :
#                  print("player wins")
#
#       elif player == "paper" and computer == "rock":
#             print("player wins")
#       else:
#          print("you lose")
#       play_again = input("play again?(y/n):").lower()
#       if not play_again =="y":
#           running = False
# print("thanks for playing")
################################## 3D Dice roller
# import random
# # print("\u25cF \u250C \u2500 \u2510 \u2502 \u2514 \u2518" ) ascii code to generate this
# # ● ┌ ─ ┐ │ └ ┘
# # "┌─────────────┐"
# # "│             │"
# # "│             │"
# # "│             │"
# # "└─────────────┘"
# dice_art ={1:( "┌─────────────┐",
#                "│             │",
#                "│       ●     │",
#                "│             │",
#                "└─────────────┘"),
#            2:(" ┌─────────────┐",
#                "│             │",
#                "│   ●   ●     │",
#                "│             │",
#                "└─────────────┘"),
#            3: ("┌─────────────┐",
#                "│    ●        │",
#                "│   ●   ●     │",
#                "│             │",
#                "└─────────────┘"),
#            4: ("┌────────────────┐",
#                "│                │",
#                "│   ●   ●        │",
#                "│   ●   ●        │",
#                "└────────────────┘"),
#            5:( "┌────────────────┐",
#                "│   ●            │",
#                "│   ●   ●        │",
#                "│   ●   ●        │",
#                "└────────────────┘"),
#            6: ("┌────────────────┐",
#                "│   ●   ●        │",
#                "│   ●   ●        │",
#                "│   ●   ●        │",
#                "└────────────────┘"),
# }
# dice =[]
# total = 0
# num_of_dice = int(input("how many dice?:"))
# for die in range (num_of_dice):
#     dice.append(random.randint(1,6))
# # for die in range (num_of_dice):
# #     for line in dice_art.get(dice[die]):
# #         print(line)
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line],end="")
#     print()
# for die in dice:
#     total += die
#     print(f"total:{total}")