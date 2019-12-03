import sys;
import math;
import random;

def main():
	print "????";

def generatePassword(_word):
	from functions import getDelimiter, getWord;
	password = _word;
	password += getDelimiter() + getWord();
	password += getDelimiter() + getWord();
	password += getDelimiter() + getWord();
	return password + getDelimiter() + str(len(password));

def getEnthropy(_word, _password):
	wordEnthropy = math.pow(52,len(_word));
	passwordEnthropy = math.pow(7776,3);
	passwordEnthropy *= math.pow(12,3);
	passwordEnthropy *= math.pow(18,2);

	return math.log((wordEnthropy * passwordEnthropy), 2);

main();

inputWord = raw_input("Enter a word that is easy to memorize for you: ");
password = generatePassword(inputWord);

print "This will be your password:";
print "\t" + password.capitalize();
print "The enthropy is rated as the following:";
print "\t" + str(getEnthropy(inputWord, password));