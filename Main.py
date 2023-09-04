import random
import os
from getpass import getpass

chances: str
word: str
numguesses: str
guesses = [] 
num_wrong: int
allowed_guesses: int

def Display_Rules() -> None:
    rules = """
    Player 1 gets to choose 5 words. 1 word will be choosen at random. Each word will be between 4 and 8 characters long

    Player 2 must select letters in the word that is presented. It will be presented as a series of underscores.
     
    The number of wrong gueses you get is equal to the chosen word + 3. You get three extra guesses.

    For each letter that player two guesses wrong, an additional body part will be drawn in

    If the entire man is drawn in, player two loses. Otherwise player one loses.

    Have fun!

    """
    print(rules)

def PickWords() -> list:
    """
    Player 1 chooses 5 words via the input. Returns a list
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Player 1: Please choose 5 words between 4 and 8 characters long")
    wordList = []
    while len(wordList) < 5:
        word = getpass("Type a word: ")
        for letter in word:
            if not letter.isalpha() or letter.isnumeric():
                print("Please only use alphabetical letters")
                continue
        if len(word) < 4 or len(word) > 8:
            print("Please enter a word between 4 and 8 characters long")
            continue
        if word in wordList:
            print("You've already used that word. Please use another")

        wordList.append(word)

    return wordList

def SetUp(words: list) -> None:
    """
    Sets up the game structure. Resets everything if game is restarted,
    """
    global word
    global chances 
    global numguesses
    global guesses 
    global num_wrong    
    global allowed_guesses

    guesses = []
    num_wrong = 0
    word = words[random.randrange(0,4)]
    allowed_guesses = len(word) + 3
    chances = ''.join(["_" for l in range(len(word))])
    numguesses = 0

def TakeTurn() -> None:
    """
    For Player two, advances a turn. Allows player two to make a guess and updates the score
    """
    global word 
    global chances
    global numguesses
    global guesses
    global num_wrong
    os.system('cls' if os.name == 'nt' else 'clear')

    Display_Hangman()

    print(" ".join([l + " " for l in chances]))
    if len(guesses) > 0:
        print("You've guessed: ", guesses)
    
    # keep checking until the player does what we want
    while True:
        guess = input("Guess a letter: ")
        print("You guessed: ", guess)
        if guess.isalpha() and not guess.isnumeric() and not len(guess) > 1:
            numguesses += 1
            guesses.append(guess)
            index = check_guessed_letter(guess)
            if index > -1:
                update_chances(guess, index)
            else:
                num_wrong += 1
            break
    print("\n")

def update_chances(letter: chr, index: int) -> None:
    "Updates the underscores and chances state variable"
    global chances
    chances = list(chances)
    chances[index] = letter
    chances = "".join(chances)


def check_guessed_letter(guess: chr) -> int:
    "Checks if the guessed letter is valid and should be updated"
    global word
    for i in range(0, len(word)):
        l = word[i]
        if guess == l and not guess == chances[i]:
            return i 
    return -1


def GameLoop() -> None:
    "The main body of the game. Continues looping until the game is over"
    while not GameOver(): 
        TakeTurn()
        if GameOver():
            break

def GameOver() -> bool:
    "Determines if the game should continue or not on each turn."
    global num_wrong
    global allowed_guesses
    global word

    if num_wrong >= allowed_guesses and "_" in chances:
            if Replay():
                SetUp(PickWords())
            else:
                return True
    elif not "_" in chances:
        if Replay():
            SetUp(PickWords())
        else: 
            return True
    return False

def Replay() -> bool:
    "Checks to see if the player wants to continue after the game has ended"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"The word was: {word}")
    Display_Hangman()
    print(" ".join([l + " " for l in chances]))
    player_input = input("Try again? y/n: ")
    if not player_input == "y" and not player_input == "n":
        print("We will take that as a 'no'...")
    replay = True if player_input == "y" else False
    if not replay:
        print("See you next time!")
    return replay

def Display_Hangman():
    global num_wrong
    global allowed_guesses

    gallos_top = "---\n    |\n    \n"

    print(f"You have used {num_wrong} attempts.\nYou have {allowed_guesses-num_wrong} attempts left")
    hangman = [" ", "-", "-", "-", "\n" , "|", " ", 
            " ", " ", "|", "\n", " ", "-", "-", "-"
            "\n", "/", "|", " ", " ", "|", "\\"
            "\n"," ", "_", "_", "_",
            "\n", "|", " ", " ", " ", "|", "\n"
            ]
    percent_array_to_display = num_wrong / allowed_guesses
    amount = (percent_array_to_display * len(hangman)) 
    split_hangman = hangman[0: int(amount)]

    print(gallos_top + "".join(split_hangman))

def Main() -> None:
    Display_Rules()
    global word
    SetUp(PickWords())
    GameLoop()

if __name__ == '__main__':
    Main()