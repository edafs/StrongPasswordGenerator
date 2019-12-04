import math;
from termcolor import colored;

# Calculates how strong a password is:
def getEntropy(_word):
	wordEnthropy = math.pow(26,len(_word));
	passwordEnthropy = math.pow(2592,3);   # words
	passwordEnthropy *= math.pow(18,4);     # delimiter
	passwordEnthropy *= 90;                 # numbers
	return math.log((wordEnthropy * passwordEnthropy), 2);

# Describes how strong the password is:
def describeEntropy(_strength):
	output = "\tThis password has an entropy of " + str(round(_strength,2));
	if _strength < 50:
		print(colored(output + ", it is weak.", "red"));
	if _strength >= 50 and _strength < 80:
		print(colored(output + ", it is secure.", "cyan"));
	if _strength >=80:
		print(colored(output + ", it is strong.", "green"));

