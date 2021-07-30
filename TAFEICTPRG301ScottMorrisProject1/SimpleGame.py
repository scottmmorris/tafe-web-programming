# Import the library that allows the generation of random numbers
import random

# Allow the user to input their name
userName = input("What is your name?: ")

# Generate magic number to be guessed
magicNum = random.randrange(1, 101, 1)

# Generate number of turns
numGuesses = random.randrange(1, 7, 1)
numTurns = numGuesses

# Initialise an outcome variable
gameWon = False

# Prompt the user to enter a number
print("Guess a number between 1 and 100")

# Loop through the turns, exiting if the user has run out of guesses or the game is won
while numTurns > 0 and gameWon == False:
    if numTurns == 1:
        print("You have " + str(numTurns) + " guess left\n")
    else:
        print("You have " + str(numTurns) + " guesses left\n")
    userGuess = int(input("What is your guess?: "))
    if userGuess > 100 or userGuess < 1:
        print("Your guess is outside the range")
    elif userGuess > magicNum:
        print("Too high")
    elif userGuess < magicNum:
        print("Too low")
    else:
        print("Correct! You win")
        gameWon = True
    numTurns -= 1

# Determine the oucome
if gameWon == True:
    outcome = "win"
else:
    outcome = "loss"

# Write the outcome to the statistics file
userGame = userName + " | " + outcome + " | " + str(numGuesses) + "\n"
statsFile = open("statistics.txt", "a")
statsFile.write(userGame)
statsFile.close()

# Display the current statistics
print("\n")
statsFile = open("statistics.txt", "r")
print(statsFile.read())
