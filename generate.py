import sys;
from termcolor import colored;

def main():
	print("????");

def generatePassword(_word):
	from functions import getDelimiter, getWord;
	_delim = getDelimiter();
	password = _word.capitalize() + _delim + getWord();
	password += _delim + getWord();
	password += _delim + getWord() + _delim;
	return password + str(len(password));

main();

inputWord = input("Enter a name that is easy to memorize for you:\t");
password = generatePassword(inputWord);


print("\nThis will be your password:");
print(colored("\t" + password, "magenta"));

from entropy import getEntropy, describeEntropy;
entropy = getEntropy(inputWord);
describeEntropy(entropy);