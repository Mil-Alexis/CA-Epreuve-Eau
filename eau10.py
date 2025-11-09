import sys

def getArguments():
    args = sys.argv[1:]
    return args

def isValidArguments(args: list):
    if len(args) != 2:
        return False
    for arg in args:
        if not arg.isdigit():
            return False
    return True

def getNumbersFromMinToMax(min: int, max: int):
    numbers = []

    for i in range(min, max +1):
        numbers.append(i)
    
    return numbers

def displayNumbersFromMinToMax():
    if not isValidArguments(getArguments()):
        return
    numbers = (getNumbersFromMinToMax(int(getArguments()[0]), int(getArguments()[1])))

    string = ""

    for number in numbers:
        string += str(number) + " "
    
    return print(string)

displayNumbersFromMinToMax()