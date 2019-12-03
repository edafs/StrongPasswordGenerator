import sys, math;

def main():
	print "????";

def generatePassword(_word):
	from functions import getDelimiter, getWord;
	_delim = getDelimiter();
	password = _word.capitalize() + _delim + getWord();
	password += _delim + getWord() + _delim;
	return password + str(len(password));

def getEnthropy(_word):
	wordEnthropy = math.pow(52,len(_word));
	passwordEnthropy = math.pow(15552,2);
	passwordEnthropy *= math.pow(18,3);
	passwordEnthropy *= math.pow(10,2);
	return math.log((wordEnthropy * passwordEnthropy), 2);

main();

inputWord = raw_input("Enter a word that is easy to memorize for you:");
password = generatePassword(inputWord);

print "This will be your password:";
print "\t" + password;
print "The enthropy is rated as the following:";
print "\t" + str(getEnthropy(inputWord));