'''
Created on Oct 15, 2010

@author: ola
'''
 
import jottoModel

filename = "kwords5.txt"

wlen = jottoModel.loadWords(filename)
print "Playing a game with ",wlen," letter words"
count = jottoModel.startGame()
print "Number of words is ",count
count = 0
while True:
    count += 1
    word = jottoModel.getGuess()
    print "My guess is '"+word+"', how many letters in common with your word: ",
    common = int(raw_input())
    if common == (wlen+1):
        print "I win!! it took me ",count," guesses"
        break

    numLeft = jottoModel.processCommon(int(common))
    print "Number of words left is",numLeft