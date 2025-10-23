import sys

def getArgument():
    args = sys.argv[1:]
    return args

def isValidArguments(args: list):
    if len(args) != 1:
        print("Un seul argument est attendu")
        return False
    if not args[0].isdigit() or int(args[0]) < 0:
        print(-1)
    