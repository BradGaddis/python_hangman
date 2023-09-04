import random

chances: str
word: str
numguesses: str
guesses = [] 

def PrintRules():
    rules = """
    Player 1 gets to choose 5 words. 1 word will be choosen at random. Each word will be between 4 and 8 characters long

    Player 2 must select letters in the word that is presented. It will be presented as a series of underscores

    For each letter that player two guesses wrong, an additional body part will be drawn in

    If the entire man is drawn in, player two loses. Otherwise player one loses.

    Have fun!

    """
    print(rules)
    return rules

def PickWords() -> list:
    
    """
    Player 1 chooses 5 words via the input. Returns a list
    """

    print("Player 1: Please choose 5 words between 4 and 8 characters long")
    wordList = []
    while len(wordList) < 5:
        word = input()
        check: bool = True
        for letter in word:
            if not letter.isalpha() or letter.isnumeric():
                check = False
        if not check:
            print("Please only use alphabetical letters")
            continue
        if len(word) < 4 or len(word) > 8:
            print("Please enter a word between 4 and 8 characters long")
            continue
        if word in wordList:
            print("You've already used that word. Please use another")

        wordList.append(word)

    return wordList

def SetUp(words: list) -> str:
    global word
    global chances 
    global numguesses
    global guesses 

    guesses = []
    word = words[random.randrange(0,4)]
    chances = ''.join(["_" for l in range(len(word))])
    numguesses = 0
    return word

def TakeTurn():
    """
    For Player two, advances a turn. Allows player two to make a guess and updates the score
    """
    global word 
    global chances
    global numguesses
    global guesses

    print("The word you're looking for is ", " ".join([l + " " for l in chances]))
    if len(guesses) > 0:
        print("You've guessed: ", guesses)
    
    # keep checking until the player does what we want
    while True:
        guess = input("Guess a letter: ")
        print("You guessed: ", guess)
        if guess.isalpha() and not guess.isnumeric() and not len(guess) > 1:
            numguesses += 1
            guesses.append(guess)
            index = checkletter(guess)
            if index > -1:
                updateChances(guess, index)
            break
    print("\n")

def updateChances(letter: chr, index: int):
    global chances
    chances = list(chances)
    chances[index] = letter
    chances = "".join(chances)

def checkletter(guess: chr):
    global word
    for i in range(0, len(word)):
        l = word[i]
        if guess == l and not guess == chances[i]:
            return i 
    return -1


def GameLoop():
    while not GameOver(): 
        TakeTurn()
        if GameOver():
            break

def GameOver():
    global numguesses
    global word
    if numguesses >= len(word) + 3 and "_" in chances:
            print("You Lose.")
            if Replay():
                SetUp(PickWords())
            else:
                return True
    elif not "_" in chances:
        print("You Win!")
        print(f"The word was: {chances}")
        if Replay():
            SetUp(PickWords())
        else: 
            return True
    return False

def Replay():
    replay = True if input("Try again? y/n: ") == "y" else False
    if not replay:
        print("See you next time!")
    return replay


def Main():
    PrintRules()
    global word
    word = SetUp(PickWords())
    GameLoop()

if __name__ == '__main__':
    Main()