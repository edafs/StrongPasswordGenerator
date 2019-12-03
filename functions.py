import sys;
import random;

# Get all the words from text file.
# The word list is originally found here:
# https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
def _initWordContents():
	wordListFileStream = open('eff_large_wordlist.txt','r');
	fileContents = wordListFileStream.readlines();
	wordListFileStream.close();
	return fileContents;

# Global Variables.
allWords = _initWordContents();
delimiters = ["~", "_", "-", "+", ",", ".", "\\", "/", "<", ">", "^", "&", "$", "%", "#", "@", "*", "!"];
secureRandom = random.SystemRandom();

# Gets a random word from the `eff_large_wordlist.txt` file.
def getWord(): 
	randomWord = secureRandom.choice(allWords);
	return randomlyCapitalize(randomWord[:-1]);
	
# Gets a random delimiter.
def getDelimiter():
	return secureRandom.choice(delimiters);

# Decides to randomly capitalize the word or not, doubles the choices.
def randomlyCapitalize(_word):
	wordChoices = [_word.capitalize(), _word];
	return secureRandom.choice(wordChoices);