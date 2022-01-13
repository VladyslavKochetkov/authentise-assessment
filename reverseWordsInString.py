from sys import argv
import re
from reverseString import reverseString

try:
    defaultArgument = argv[1]
except IndexError:
    defaultArgument = "Demo string to reverse."

noneWordMatch = re.compile("\W")
def reverseWordsInString(stringToReverse = defaultArgument):
    hasPunctuationAtEnd = noneWordMatch.match(stringToReverse[-1]) is not None
    if hasPunctuationAtEnd:
        punctuationAtEnd = stringToReverse[-1]
        stringToReverse = stringToReverse[0:len(stringToReverse) - 1]

    reversedString = " ".join(list(map(reverseString, stringToReverse.split())))
    if hasPunctuationAtEnd:
        reversedString += punctuationAtEnd
    print(reversedString)

if argv[0] == "reverseWordsInString.py":
    reverseWordsInString()