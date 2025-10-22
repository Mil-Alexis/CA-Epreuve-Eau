import sys

#Utils

def splitArguments(args: list):
	splittedArguments = []

	for arg in args:
		if ' ' in arg:
			splittedArguments.extend(arg.split())
		else:
			splittedArguments.append(arg)
			
	return splittedArguments

#Parsing

def getArguments():
	args = splitArguments(sys.argv[1:])
	return args

#Error Handling

def isValidArguments(args: list):
	if len(args) < 2:
		print("Au moins 2 arguments sont attendus")
		return False
	else:
		return True

#Resolve

def reverseArguments(args: list):
	reversedArguments = []
	for i in range(-1, -len(args)-1, -1):
		reversedArguments.append(args[i])

	return reversedArguments

#Display

def displayReversedArguments():
	if not isValidArguments(getArguments()):
		return
	print(reverseArguments(getArguments()))

displayReversedArguments()



