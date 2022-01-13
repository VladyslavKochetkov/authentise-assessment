from reverseString import reverseString
from reverseOrderOfWordsInString import reverseOrderOfWordsInString
from getCommandLineInputs import getCommandLineInputs
from operator import itemgetter

helpString = """Usage: python3 reverseLettersOrWordsFromFile.py 'input.txt' -(r|w)
-r reverse the letters in the string
-w reverse order of words in a string"""

flag, stringOrFile = itemgetter("flag", "stringOrFile")(getCommandLineInputs(helpString))

fileStream = open(stringOrFile, "r")
fileText = fileStream.read()
fileStream.close()

print(reverseString(fileText) if flag == "-r" else reverseOrderOfWordsInString(fileText))