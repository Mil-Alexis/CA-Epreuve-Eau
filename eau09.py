import sys

def getArguments():
    args = sys.argv[1:]
    return args

def isValidArguments(args: list):
    if len(args) < 1:
        return False
    return True

def containsOnlyDigit(args: list):
    for arg in args:
        for char in arg:
            if not char.isdigit() and char != " ":
                return False
    return True

def displayIfOnlyDigit():
    if not isValidArguments(getArguments()):
        return
    return print(containsOnlyDigit(getArguments()))

displayIfOnlyDigit()