import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

wins = 0
loses = 0
draws = 0

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalis Input. Try again...")
        continue

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors)\
        or (player_move == paper and computer_move == rock)\
        or (player_move == scissors and computer_move == paper):
        print("You win!")
        wins += 1
    elif player_move == computer_move:
        print("Draw!")
        draws += 1
    else:
        print("You lose!")
        loses += 1

    print(f"Results: Wins: {wins}; Loses: {loses}; Draws: {draws}")

    break_game_flag = False
    while True:
        play_again = input("Type [yes] to Play Again or [no] to quit: ")

        if play_again.lower() == "yes":
            break
        elif play_again.lower() == "no":
            break_game_flag = True
            break
        else:
            print("Invalid input. Please try again...")
            continue

    if break_game_flag:
        raise SystemExit("Thank you for playing!")
