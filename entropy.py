import math;

# Calculates how strong a password is:
def getEntropy(_word):
	wordEnthropy = math.pow(26,len(_word));
	passwordEnthropy = math.pow(15552,2);   # words
	passwordEnthropy *= math.pow(18,3);     # delimiter
	passwordEnthropy *= 90;                 # numbers
	return math.log((wordEnthropy * passwordEnthropy), 2);

# Describes how strong the password is:
def describeEntropy(_strength):
    from termcolor import colored;
    if _strength < 40:
        print(colored("\tThis password is weak.", "red"));
    if _strength >= 40 and _strength < 70:
        print(colored("\tThis password is okay.", "yellow"));
    if _strength >= 75:
        print(colored("\tThis password is secure.", "cyan"));

