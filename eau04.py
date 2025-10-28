import sys


def getArguments():
    args = sys.argv[1:]
    return args

def isValidArguments(args: list):
    if len(args) != 1:
        print("Un seul argument est attendu")
        return False
    elif not args[0].isdigit() or int(args[0]) < 0:
        print(-1)
        return False
    else:
        return True

def getFibonacciNumberAtIndex(number: int):
    if number == 0 or number == 1:
        return number

    n1 = 0
    n2 = 1

    for n in range(1, number):
        n = n1 + n2
        n1 = n2
        n2 = n
    return n

def displayFibonacciNumberAtIndex():
    if not isValidArguments(getArguments()):
        return
    number = int(getArguments()[0])
    print(getFibonacciNumberAtIndex(number))

displayFibonacciNumberAtIndex()
