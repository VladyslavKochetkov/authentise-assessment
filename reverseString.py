from sys import argv

try:
    defaultArgument = argv[1]
except IndexError:
    defaultArgument = "Demo string to reverse"

def reverseString(stringToReverse = defaultArgument):
    reversedString = stringToReverse[::-1]
    return reversedString

if argv[0] == "reverseString.py":
    print('Reversed string from "{original}" to "{reversed}"'.format(original = defaultArgument, reversed = reverseString()))