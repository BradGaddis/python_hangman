import random

def PickWords():
    print("Player 1: Please choose 5 words between 4 and 8 characters long")
    wordList = []
    while len(wordList) < 5:
        word = input().lower()
        if len(word) < 4 or len(word) > 8:
            print("Please enter a word between 4 and 8 characters long")
            continue
        if word in wordList:
            print("You've already used that word. Please use another")

        wordList.append(word)
    return wordList

def GetRandomWord(words: list):
    return words[random.randrange(0,4)]

def TakeTurn():
    pass

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

def GameOver(numWrongGuesses: int, numCorrectGuesses: int):
    return False


def Main():
    PrintRules()
    word = GetRandomWord(PickWords())
    print(word)



if __name__ == '__main__':
    Main()