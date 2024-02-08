"""
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string.
Examples: 
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
"""

def capitalizes(string):
    words = string.split()
    for word in words:
        words[words.index(word)] = word.capitalize()
    print(" ".join(words))
    return " ".join(words)

while True:
    string = str(input("Enter a string: "))
    capitalizes(string)