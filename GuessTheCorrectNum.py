from random import randint as r

def Results(player1Attempts,player2Attempts,player1Name,player2Name):
    if player1Attempts < player2Attempts:
        print(f"Congratulations {player1Name}! YOU WON THE MATCH by {player1Attempts} Attempts.")
        print(f"Well Try {player2Name}! You defeated by {player2Attempts} Attempts. BETTER LUCK NEXT TIME")

    elif player1Attempts < player2Attempts:
        print(f"Congratulations {player2Name}! YOU WON THE MATCH by {player2Attempts} Attempts.")
        print(f"Well Try {player1Name}! You defeated by {player1Attempts} Attempts. BETTER LUCK NEXT TIME")

    else:
        print(f"Congratulations Both Players {player1Name},{player2Name}! Both Are Guessed with same Attempts. So, TRY TO PLAY AGAIN.")

# Player-1 ==> It will check the guessed number is Correct or wrong 
def Player1NumChecker(num,MachineNum,playerName):
    if(num == MachineNum):
        return f"Correct Guess {playerName}."
    elif(num < MachineNum):
        return f"Guessed Number is TOO LOW! TRY AGAIN."
    elif(num > MachineNum):
        return f"Guessed Number is TOO HIGH! TRY AGAIN."

# Player-2 ==> It will check the guessed number is Correct or wrong
def Player2NumChecker(num,MachineNum,playerName):
    # simple If-Else Condition
    if (num == MachineNum):
        return f"Correct Guess! You Won the Match {playerName}."
    elif (num < MachineNum):
        return f"Guess Number is TOO LOW! BETTER LUCK NEXT TIME."
    elif (num > MachineNum):
        return f"Guess Number is TOO HIGH! BETTER LUCK NEXT TIME."

# It is our main part to execute perfectly 
def DiceGame():

    print("WELCOME TO GUESS THE NUMBER GAME....... ")

    print("INSTRUCTIONS:")
    print("1.Two Players are required to play this game.")
    print("2.Initially, my BUDDY Display a number within range then you need to guess that number.")
    print("3.Player1 Start the Game First")
    print("4.Next, Player2 Turn")

    print("Note: 1.player can guess any number of times specified within the range \n\t 2.Number of guesses will count each player")


    print("Now, You Have to Enter two players Here!")

    # Takes player1 name as input
    player1 = input("Enter First player name: ")
    print(f"Successfully Added You As {player1}")

    # Takes player2 name as input
    player2 = input("Enter Second player name: ")
    print(f"Successfully Added You As {player2}")

    print("Before Start Game, Please specify Range (ex.1-20,30-40...etc)")

    # these are the Lower and Upperboundries
    MinNum = int(input("Enter Minimum Range: "))
    MaxNum = int(input("Enter Maximum Range: "))

    # Initialize attempts with Zero
    player1Attempts = 0
    player2Attempts = 0

    # Here,Buddy will generate Numbers within the range
    BuddyGuessNum1 = r(MinNum,MaxNum)
    BuddyGuessNum2 = r(MinNum, MaxNum)

    print("My Buddy Guessed two numbers....Try To Guess")

    Running = True

# Player-1 play until the guessed number is Correct
    print(f"Dear {player1}, Guess a number between {MinNum} - {MaxNum}")
    while(Running):

        #  It keep track our Each and every attempt
        player1Attempts += 1

        guessNum = input(f"Guess A number {player1}:")

        guessNum = int(guessNum)

        print(Player1NumChecker(guessNum,BuddyGuessNum1,player1))
        
        # Guessed Number is Correct then it will terminate loop
        if(guessNum == BuddyGuessNum1):
            break

    print("Now, Player2 Turn....")

    # Player-1 play until the guessed number is Correct
    print(f"Dear {player2}, Guess a number between {MinNum} - {MaxNum}")
    while (Running):
        #  It keep track our Each and every attempt
        player2Attempts += 1

        guessNum = input(f"Guess A number {player2}:")

        guessNum = int(guessNum)

        print(Player2NumChecker(guessNum, BuddyGuessNum2, player2))

        # Guessed Number is Correct then it will terminate loop
        if (guessNum == BuddyGuessNum2):
            break

    print("Now, RESULTS Time......")

    # Results is a funtion that announce or decleare the winner
    Results(player1Attempts,player2Attempts,player1,player2)

DiceGame()









