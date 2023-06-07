import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

wins = 0
loses = 0
draws = 0

def player_turn(player_move):
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalis Input. Try again...")
        return True

    return player_move

def computer_move():
    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")
    return computer_move

def analizating_resule():
    wins = 0
    loses = 0
    draws = 0

    player_move = player_turn(input("Choose [r]ock, [p]aper or [s]cissors: "))

    if player_move == True:
        return wins, loses, draws, True

    computer = computer_move()

    if (player_move == rock and computer == scissors)\
        or (player_move == paper and computer == rock)\
        or (player_move == scissors and computer == paper):
        print("You win!")
        wins += 1
    elif player_move == computer:
        print("Draw!")
        draws += 1
    else:
        print("You lose!")
        loses += 1

    return wins, loses, draws, False

def play_again_checking(play_again):
    while True:
        if play_again.lower() == "yes":
            return True
        elif play_again.lower() == "no":
            raise SystemExit("Thank you for playing!")
        else:
            print("Invalid input. Please try again...")
            play_again = input("Type [yes] to Play Again or [no] to quit: ")
            continue

while True:

    wins_values, loses_values, draws_values, flag_result = analizating_resule()

    if flag_result:
        continue

    wins += wins_values
    loses += loses_values
    draws += draws_values

    print(f"Results: Wins: {wins}; Loses: {loses}; Draws: {draws}")

    play_again = play_again_checking(input("Type [yes] to Play Again or [no] to quit: "))

    if play_again:
        continue