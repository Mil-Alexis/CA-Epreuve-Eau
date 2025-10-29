import sys

def getArguments():
	args = sys.argv[1:]
	return args

def isValidArguments(args: list):
	if len(args) != 2:
		print("error")
		return False
	return True

def isStringInString(firstString: str, secondString: str):

	firstString = list(firstString)
	secondString = list(secondString)

	for i in range(0, len(firstString)):
		for i in range(0, len(secondString)):
			if len(firstString) < len(secondString):
				return False
			if firstString[i] != secondString[i]:
				firstString.pop(0)

	return True


def displayIfStringInString():
    if not isValidArguments(getArguments()):
        return
    print(isStringInString(getArguments()[0], getArguments()[1]))

displayIfStringInString()