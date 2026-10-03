# imagine wordle

word = "emoji"

# The user guess is...

guess = input(" Please give me a word that is FIVE letters long and the word CANNOT have one letter MORE than ONCE: ")

# Determine what the guess resulted in this format
# For example if they put store

# Grey
# Grey
# Green
# Grey
# Yellow
import sys
if len(guess) != 5 and not guess.isalpha() : 
    sys.exit("Invalid word choice, it must be exactly 5 letters and only letters")

# Check if the guess is all letter only, if not then exit te program
for i in range(5):   
    # check each letter if it is yellow or green or grey
    if word[i] == guess[i]:
        print("green") 
     
    elif guess[i] in word:
        print("yellow")

    else:
        print("grey")
        