from sys import argv

try:
    defaultArgument = argv[1]
except IndexError:
    defaultArgument = "Demo string to reverse"

def reverseString(stringToReverse = defaultArgument):
    reversedString = stringToReverse[::-1]
    print("Reversed string from {original} to {reversed}".format(original = stringToReverse, reversed = reversedString))
    return reversedString


reverseString()