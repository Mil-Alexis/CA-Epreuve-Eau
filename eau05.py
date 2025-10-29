import sys

def getArguments():
    args = sys.argv[1:]
    return args

def isPrimeNumber(number: int):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def isValidArguments(args: list):
    if len(args) != 1:
        print("Un seul argument est attendu")
        return False
    elif not args[0].isdigit() or int(args[0]) < 0:
        print(-1)
        return False
    else:
        return True

def getNexPrimeNumber(number: int):

    number += 1

    while not isPrimeNumber(number):
        number += 1
    return number


def displayNextPrimeNumber():
    if not isValidArguments(getArguments()):
        return
    number = int(getArguments()[0])
    print(getNexPrimeNumber(number))

displayNextPrimeNumber()


