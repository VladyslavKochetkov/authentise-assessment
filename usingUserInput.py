from reverseString import reverseString
from reverseOrderOfWordsInString import reverseOrderOfWordsInString
from reverseWordsInString import reverseWordsInString

fileOrInput = None

print("This is an bonus part of the assignment, where the user can enter all their choices using the command line.")
isFirstRun = True
while fileOrInput is None:
    print('Invalid input. Please enter either "file" or "input".' if not isFirstRun else 'Do you want to enter a string or read from a file? Enter "file" or "input".')
    userInput = input("Enter: ")
    isFirstRun = False
    if userInput == "file" or userInput == "input":
        fileOrInput = userInput
        break;

stringToReverse = None
isFirstRun = True
while stringToReverse is None:
    print("We couldn't read that file. Please try another." if not isFirstRun else "Please enter the {fileOrInput} you want to modify.".format(fileOrInput = fileOrInput))
    userInput = input("Enter: ")
    isFirstRun = False
    if fileOrInput == "file":
        try:
            fileStream = open(userInput, "r")
            stringToReverse = fileStream.read()
            fileStream.close()
        except FileNotFoundError:
            print("File entered doesn't exist.")
            continue
        except Exception as e:
            print("General error reading file.")
            print(e)
            continue
    else:
        stringToReverse = userInput

while True:
    print('What action do you want to perform? Enter "r" to reverse the string, "w" to reverse the order of words in the string, or "rw" to reverse the words in the string.')
    userInput = input("Enter: ")
    if userInput == "r":
        print('Reversed the string from "{original}" to "{reversed}"'.format(original = stringToReverse, reversed = reverseString(stringToReverse)))
        break;
    elif userInput == "w":
        print('Reversed the order of words in the string from "{original}" to "{reversed}"'.format(original = stringToReverse, reversed = reverseOrderOfWordsInString(stringToReverse)))
        break;
    elif userInput == "rw":
        print('Reversed the words in the string from "{original}" to "{reversed}"'.format(original = stringToReverse, reversed = reverseWordsInString(stringToReverse)))
        break;
    else:
        print('Invalid input. Please enter either "r", "rw", or "w".')