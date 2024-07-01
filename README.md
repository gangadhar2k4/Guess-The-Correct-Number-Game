# Guess-The-Correct-Number-Game
This is a Python program for a number guessing game between two players. Here's a breakdown of the code:

Functions:

1. Results: Announces the winner and displays the number of attempts taken by each player.
2. Player1NumChecker and Player2NumChecker: Check if the guessed number is correct, too low, or too high and return a corresponding message.
3. DiceGame: The main function that executes the game.

Game Flow:

1. The program welcomes the players and displays instructions.
2. It asks for the names of the two players and stores them as player1 and player2.
3. The program asks for a range (minimum and maximum numbers) and generates two random numbers within that range using the randint function from the random module. These numbers are stored as BuddyGuessNum1 and BuddyGuessNum2.
4. The program initializes the number of attempts for each player to 0.
5. Player 1 is prompted to guess a number, and their attempt is checked using Player1NumChecker. If the guess is correct, the loop breaks.
6. Player 2 is prompted to guess a number, and their attempt is checked using Player2NumChecker. If the guess is correct, the loop breaks.
7. The Results function is called to announce the winner and display the number of attempts taken by each player.

Notes:

- The program uses a while loop to keep track of the attempts for each player.
- The input function is used to get user input (guesses) and convert them to integers using int().
- The program uses f-strings to format the output messages.
- The randint function is used to generate random numbers within the specified range.

Overall, this program implements a simple number guessing game between two players, with the goal of guessing a randomly generated number within a specified range.
