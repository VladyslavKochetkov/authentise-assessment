from sys import argv
import re
from reverseString import reverseString

try:
    defaultArgument = argv[1]
except IndexError:
    defaultArgument = "Demo string to reverse."

noneWordMatch = re.compile("\W")
def reverseOrderOfWordsInString(stringToReverse = defaultArgument):
    hasPunctuationAtEnd = noneWordMatch.match(stringToReverse[-1]) is not None
    if hasPunctuationAtEnd:
        punctuationAtEnd = stringToReverse[-1]
        stringToReverse = stringToReverse[0:len(stringToReverse) - 1]

    reversedString = " ".join(stringToReverse.split()[::-1])
    if hasPunctuationAtEnd:
        reversedString += punctuationAtEnd
    return reversedString

if argv[0] == "reverseOrderOfWordsInString.py":
    print('Reversed the order of words in string from "{original}" to "{reversed}"'.format(original = stringToReverse, reversed = reverseOrderOfWordsInString()))