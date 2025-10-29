import sys

def getArguments():
	args = sys.argv[1:]
	return args

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

def alternateUpperAndLower(args: list):

	isUpper = False

	string = ""

	for arg in args:
		for char in arg:
			if not isUpper:
				string += char.upper()
				isUpper = True
			else:
				string += char.lower()
				isUpper = False
		string += " "
	return string

def displayalternateUpperAndLower():
    if not isValidArguments(getArguments()):
        return
    print(alternateUpperAndLower(getArguments()))

displayalternateUpperAndLower()