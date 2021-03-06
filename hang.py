import random
import string
import os

WORDLIST_FILENAME = "words.txt"
NUMER_GUESSES = 8

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print 'Loading word list from file...'
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def validWord(guessWord, guesses):
    letter = string.ascii_lowercase
    differentLetters = []
    for letter in guessWord:
        if letter not in differentLetters:
            differentLetters.append(letter)

    if len(differentLetters) > guesses:
        print 'The number of Different Letters it is more than number of Guesses'
        return False

    print 'Number of Different Letters:', len(differentLetters), '.'
    return True

def chooseAWord(wordlist, guesses):
    chosenWord = random.choice(wordlist)
    if validWord(chosenWord, guesses):
        return chosenWord
    chooseAWord(wordlist, guesses)

def isWordGuessed(secretWord, lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

def updateAvailableLetter(availableLetters, lettersGuessed):
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '')
    return availableLetters

def validLetter(letter, lettersGuessed):
    if letter in lettersGuessed:
        return False
    return True

def printSecretWord(lettersGuessed, secretWord):
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_'
        print word

def hangman(secretWord):
    guesses = NUMER_GUESSES
    lettersGuessed = []

    print 'Welcome to the game, Hangmam!'
    print 'I am thinking of a word that is', len(secretWord) ,' letters long.'
    print '-------------'

    word = printSecretWord(lettersGuessed, secretWord)
    availableLetters = getAvailableLetters()

    while isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        print 'Available letters', availableLetters
        word = printSecretWord(lettersGuessed, secretWord)
        letter = raw_input('Please guess a letter: ')

        if validLetter(letter, lettersGuessed) is True:
            if letter in secretWord:
                os.system('clear')
                print 'Good Guess: '
                lettersGuessed.append(letter)

            else:
                guesses -= 1
                lettersGuessed.append(letter)
                os.system('clear')
                print 'Oops! That letter is not in my word \n',

        else:
                os.system('clear')
                print 'Oops! You have already guessed that letter \n',


        availableLetters = updateAvailableLetter(availableLetters, lettersGuessed)
        print '------------ \n'


    if isWordGuessed(secretWord, lettersGuessed) is True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

wordlist = loadWords()
secretWord = chooseAWord(wordlist, NUMER_GUESSES).lower()
hangman(secretWord)
