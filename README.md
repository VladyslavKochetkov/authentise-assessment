# Authentise Challenge

All the assignments are written using python3

## Part One

To execute this part of the assignment run `python3 reverseString.py`.

By default it will reverse the string `Demo string to reverse`, however it can also take
a command line argument such as `python3 reverseString.py "Some other string to reverse"`.

### Examples

_Default argument_

> Input: `python3 reverseString.py`
>
> Output: `Reversed string from "Demo string to reverse" to "esrever ot gnirts omeD"`

_Custom argument_

> Input: `python3 reverseString.py "Reversing a custom argument"`
>
> Output: `Reversed string from "Reversing a custom argument" to "tnemugra motsuc a gnisreveR"`

## Part Two

To execute this part of the assignment run `python3 reverseOrderOfWordsInString.py`.

This assignment also has a default argument of `Demo string to reverse.` and also allows for a custom argument to be passed in such as above.

There is also some bonus handling of punctuation, if you the string with a puncuation, it will stay at the end.

### Examples

_Default argument_

> Input: `python3 reverseOrderOfWordsInString.py`
>
> Output: `Reversed the order of words in string from "Demo string to reverse." to "reverse to string Demo."`

_Custom argument_ [We escape the ! in bash]

> Input: `python3 reverseOrderOfWordsInString.py "Reverse a custom argument\!"`
>
> Output: `Reversed the order of words in string from "Reverse a custom argument!" to "argument custom a Reverse!"`

## Part Two (Bonus)

I initially misread the assignment and thought that the words in the string should be reversed themselves, not the order of the words. This part reversed the order of the words, but not the words themselves.

Once again the default argument is `Demo string to reverse.` but can be changed by passing an argument.

### Examples

_Default argument_

> Input: `python3 reverseWordsInString.py`
>
> Output: `Reversed each word in the string from "Demo string to reverse." to "omeD gnirts ot esrever."`

_Custom argument_ [We escape the ! in bash]

> Input: `python3 reverseWordsInString.py "Reverse a custom argument\!"`
>
> Output: `Reversed each word in the string from "Reverse a custom argument!" to "esreveR a motsuc tnemugra!"`

## Part Three

In this assignment you pass in the word and a flag (either -r or -w, but not both) in the command line and it executes accordingly.

We handle the following errors and print the reason for the error and a general help message.

- Not a total of two arguments are passed into the script (ignoring the default argument of the calling file name)
- Of those two arguments both are a flag, such as `python3 commandLineReverseLettersOrWords.py -r -w`
- None of the arguments passed are a flag, meaning there are two strings instead of one, or an unknown arugment.

The order of the arguments doesn't matter, both of the following are valid `python3 commandLineReverseLettersOrWords.py "Reverse this" -r` and `python3 commandLineReverseLettersOrWords.py -r "Reverse this"`.

### Examples

_Reversing a string_

> Input: `python3 commandLineReverseLettersOrWords.py "Reverse this" -r`
>
> Output: `Reversed the order of the string from "Reverse this" to "siht esreveR"`

_Reversing order of words_

> Input: `python3 commandLineReverseLettersOrWords.py "Reverse this but with some extra words" -w`
>
> Output: `Reversed the order of the words in the string from "Reverse this but with some extra words" to "words extra some with but this Reverse"`

_Invalid input [Incorrect argument count]_

> Inputs: `python3 commandLineReverseLettersOrWords.py` or `python3 commandLineReverseLettersOrWords.py "Hello"` or `python3 commandLineReverseLettersOrWords.py -r`
>
> Output:
>
> `Expected two arguments to be passed`
>
> `Usage: python3 commandLineReverseLettersOrWords.py 'String to modify' -(r|w)`
>
> `-r reverse the letters in the string`
>
> `-w reverse order of words in a string`

_Invalid input [No flag]_

> Inputs: `python3 commandLineReverseLettersOrWords.py "Hello" "Again"`
>
> Output:
>
> `Expected to receive flag either -r or -w, but instead for two strings`
>
> `Usage: python3 commandLineReverseLettersOrWords.py 'String to modify' -(r|w)`
>
> `-r reverse the letters in the string`
>
> `-w reverse order of words in a string`

_Invalid input [Multiple flags]_

> Inputs: `python3 commandLineReverseLettersOrWords.py -r -w`
>
> Output:
>
> `Received two flag arguments -r and -w, only expected one`
>
> `Usage: python3 commandLineReverseLettersOrWords.py 'String to modify' -(r|w)`
>
> `-r reverse the letters in the string`
>
> `-w reverse order of words in a string`

## Part Four

For this assignment we refactored the part three assignment and move the command line argument processessing outside of the assignment script.

### Examples

_Reversing a string_

> Input: `python3 reverseLettersOrWordsFromFile.py "inputfile.txt" -r`
>
> Output:
>
> `Reversed the file using the order of the string from`
>
> `---ORIGINAL---`
>
> `Hello this is a demo file.`
>
> `---END ORIGINAL---`
>
> `to`
>
> `---REVERSED---`
>
> `.elif omed a si siht olleH`
>
> `---END REVERSED---`

_Reversing order of words_

> Input: `python3 reverseLettersOrWordsFromFile.py "inputfile.txt" -w`
>
> Output:
>
> `Reversed the file using the order of the words in the string from`
>
> `---ORIGINAL---`
>
> `Hello this is a demo file.`
>
> `---END ORIGINAL---`
>
> `to`
>
> `---REVERSED---`
>
> `file demo a is this Hello.`
>
> `---END REVERSED---`

### Part Five (Extra)

You can also use all of these using a command where you are asked your intents.

#### Example

By running `python3 usingUserInput.py` you will be asked to enter all of the possible variables of inputs and string manipulation.

```
This is an bonus part of the assignment, where the user can enter all their choices using the command line.
Do you want to enter a string or read from a file? Enter "file" or "input".
> Enter: file
Please enter the file you want to modify.
> Enter: inputfile.txt
What action do you want to perform? Enter "r" to reverse the string, "w" to reverse the order of words in the string, or "rw" to reverse the words in the string.
> Enter: rw
Reversed the words in the string from "Hello this is a demo file." to "olleH siht si a omed elif."
```
