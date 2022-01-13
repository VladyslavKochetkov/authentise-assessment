from reverseString import reverseString
from reverseOrderOfWordsInString import reverseOrderOfWordsInString
from getCommandLineInputs import getCommandLineInputs
from operator import itemgetter

helpString = """Usage: python3 commandLineReverseLettersOrWords.py 'String to modify' -(r|w)
-r reverse the letters in the string
-w reverse order of words in a string"""

flag, stringOrFile = itemgetter("flag", "stringOrFile")(getCommandLineInputs(helpString))

print(reverseString(stringOrFile) if flag == "-r" else reverseOrderOfWordsInString(stringOrFile))