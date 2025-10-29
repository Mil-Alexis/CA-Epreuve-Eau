import sys

def getArguments():
	args = splitArguments(sys.argv[1:])
	return args

def splitArguments(args: list):
	splittedArguments = []

	for arg in args:
		if ' ' in arg:
			splittedArguments.extend(arg.split())
		else:
			splittedArguments.append(arg)
			
	return splittedArguments

def isValidArguments(args: list):
	if len(args) < 1:
		print("error")
		return False
	else:
		for arg in args:
			if arg.isdigit():
				print(arg)
				return False
	return True

def firstLetterUpper(args: list):

	string = ""

	for arg in args:
		for i in range(0, len(arg)):
			if i == 0:
				string += arg[i].upper()
			else:
				string += arg[i].lower()
		string += " "

	return string

def displayFirstLetterUpper():
    if not isValidArguments(getArguments()):
        return
    print(firstLetterUpper(getArguments()))

displayFirstLetterUpper()