'''
Created on Oct 15, 2010

@author: ericmercer
'''
import random

wordList = []
guessList = []
possibleList = []

def loadWords(filename):
    """
    Given the name of a file that contains a list of words, 
    one per line and all the same length, read the contents 
    of the file into a list of strings.
    Returns length of the words contained in the file
    """
    global wordList
    file = open(filename)
    wordList = [ word.strip() for word in file ]
    file.close()
    return len(wordList[0])
    
def startGame():
    """
    Set up any state that your player needs in order to play the game. 
    For example, create an empty list to represent all the guesses made 
    during a game (the list would be added to by other functions in the
    module).
    Returns number of words the secret word could be.
    """
    global wordList
    global possibleList
    for word in wordList:
        possibleList.append(word)
    return len(possibleList)

def getGuess():
    """
    Returns a word from the remaining possible choices.
    """
    global possibleList
    global guessList
    guess = random.choice(possibleList)
    guessList.append(guess)
    return guess
    
def processCommon(common):
    """
    Given number of letters in common between the last guess and the secret word
    reduce the possible words remaining for guessing to just those that could be 
    the secret word.
    The parameter given is a tuple of integers that represent the common count: 
     - the first number is count of the letters that are in same positions
     - the second count is count of the letters that are in different positions
    Returns number of words remaining that could be secret word.
    """
    global possibleList
    global guessList
    remainingList = []
    for word in possibleList:
        if word != guessList[-1] and commonCount(word, guessList[-1]) == common:
            remainingList.append(word)
    possibleList = remainingList        
    return len(possibleList)

def commonCount(a,b):
    """
    Returns number of letters in common between given strings a and b,
    no matter where those letters occur within the strings
    """
    alist = list(a)
    blist = list(b)
    for c in alist:
        if c in blist:
            blist[blist.index(c)] = '*'
    return blist.count("*")