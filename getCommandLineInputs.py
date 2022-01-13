from sys import argv
import re

def getCommandLineInputs(helpString):
    if len(argv) != 3:
        print("Expected two arguments to be passed\n{help}".format(help = helpString))
        exit(-1)

    flagRegex = re.compile("-(r|w)")
    flag = None
    flagIndex = 0
    for i in range(1, len(argv)):
        if flagRegex.match(argv[i]) is not None:
            if flag is not None:
                print(
                    "Received two flag arguments {first_flag} and {second_flag}, only expected one\n{help}".format(
                        first_flag = flag, 
                        second_flag = argv[i], 
                        help = helpString)
                    )
                exit()
            flag = argv[i]
            flagIndex = i
    if flag is None:
        print("Expected to receive flag either -r or -w, but instead for two strings\n{help}".format(help = helpString))
        exit(-1)
        

    return {
        "stringOrFile": argv[2] if flagIndex == 1 else argv[1],
        "flag": flag
    }