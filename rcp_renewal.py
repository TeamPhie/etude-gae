import random
same_list = [[0, 0], [1, 1], [2, 2]]
win_list = [[0, 1], [1, 2], [2, 0]]
lose_list = [[0, 2], [1, 0], [2, 1]]
computer = random.randint(0, 2)
player = input()
if player == "Goo":
    player_number = 0
elif player == "Chii":
    player_number = 1
elif player == "Par":
    player_number = 2
else:
    print("Goo or Chii , Par plese...")
rcp_list = [player, computer]

