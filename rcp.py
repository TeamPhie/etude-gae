import random

player = input()
computer = random.randint(0, 2)

if player == "Goo":
    player_number = 0
    if computer == 0:
        print("aikoでしょ")
    elif computer == 1:
        print("YOU WIN!!")
    else:
        print("YOU LOSE..")
elif player == "Chii":
    player_number = 1
    if computer == 0:
        print("YOU LOSE..")
    elif computer == 1:
        print("aikoでしょ")
    else:
        print("YOU WIN!!")
elif player == "Par":
    player_number = 2
    if computer == 0:
        print("YOU WIN!!")
    elif computer == 1:
        print("YOU LOSE..")
    else:
        print("aikoでしょ")
else:
    print("Goo or Chii , Par plese...")
