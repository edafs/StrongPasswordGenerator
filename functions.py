import sys;
import random;


# Get all the Ids from text file:
def _initWordContents():
	wordListFileStream = open('eff_large_wordlist.txt','r');
	fileContents = wordListFileStream.readlines();
	wordListFileStream.close();
	return fileContents;

# Global Variables.
allWords = _initWordContents();
delimiters = ["~", "_", "-", "+", ",", ".", "\\", "/", "<", ">", "^", "&"];

# Gets a random word from the `eff_large_wordlist.txt` file.
def getWord():
	randomWord = random.choice(allWords);
	return randomWord[:-1];

# Gets a random delimiter.
def getDelimiter():
	return random.choice(delimiters);
