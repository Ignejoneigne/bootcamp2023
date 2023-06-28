#TASK 1: make game replayable by asking o continue at the end
#TASK 2: make max_number as input by a player
#TASK 3: store played games to dictionary in a form player_name: [max_number, attempts(guessed with)]

import random

def play_game():
    name = input('Please provide your name: ')
#Making max_number as a input (TASK2)
    max_number = int(input('Please enter the maximum number for the game: '))
    number = random.randint(1, max_number + 1)
    attempt = 0

    game = True
    while game:
        attempt =+ 1
        guess = int(input(f'{name}, enter your guess {attempt}: '))
        if guess > number:
            print('Your guess is higher. Try again.')
        elif guess < number:
            print('Your guess is lower. Try again.')
        else:
            print(f'You won! It took you {attempt} attempt(s).')
            game = False

#Store played games to dictionary (TASK3)
    if name in game_stats: #game_stats is dictionary that is a list of tuples and stores game attempts for eash player.
        game_stats[name].append((max_number, attempt))
    else:
        game_stats[name] = [(max_number, attempt)]

#Making game replayable (TASK1)
    play_again = input('Would you like to play again? (yes/no): ')
    if play_again.lower() == "yes":
        play_game()
    else:
        print('Thank you for playing. Bye Bye!')
        print('Game statistics: ')
        for player, games in game_stats.items():
            print(f"Player: {player}")
            for i, game in enumerate(games):
                print(f"Game {i+1} - Max Number: {game[0]}, Attempts: {game[1]}")

game_stats = {}
play_game()




