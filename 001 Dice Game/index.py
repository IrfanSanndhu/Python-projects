import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

def if_win():
    if max(players_score) > 50:
        winning_idx = players_score.index(max(players_score))
        print("Player number: ", winning_idx + 1, "is the winner with a score of: ", max(players_score))
    else:
        return 

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be 2 - 4 players")
    else:
        print("Invalid, Try again")

max_score = 50
players_score = [0 for _ in range(players)]
print(players_score)

while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nplayer number ", player_idx + 1, "turn has been started!\n")
        print("Your total score is: ", players_score[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)?: ")
            if should_roll.lower() != "y":
                if_win()
                break
            else:
                value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                if_win()
                break
            else:
                current_score += value
                print("You rolled a: ", value)
                print("your score is:", current_score)
        players_score[player_idx] += current_score
        print("Your total score is: ", players_score[player_idx])
