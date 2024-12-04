import random
from random import shuffle

# Function to shuffle the ball
def shuffle_ball():
    blist = ["", "O", ""]
    shuffle(blist)
    return blist

# Function to get the player's guess
def p_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Hi, what's your guess for the ball? 0, 1, or 2: ")
    return int(guess)

# Function to check the player's guess
def check_guess(blist, guess):
    if blist[guess] == "O":
        print("You won this round!")
    else:
        print("Big L")
    
    print("Here was the final shuffle: ", blist)

# Main program flow
if __name__ == "__main__":
    # SHUFFLE LIST
    shuffled_list = shuffle_ball()
    # USER GUESS
    guess2 = p_guess()
    # CHECK GUESS
    check_guess(shuffled_list, guess2)
