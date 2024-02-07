"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
"""
def count(sentence):
    upperSentence = sentence.upper()
    vowels = "AEIOU"
    count = 0
    repeated_vowels = set()
    
    for char in upperSentence:
        if char in vowels and char not in repeated_vowels:
            count += 1
            repeated_vowels.add(char)
    
    print(count)
    return count

while True:
    sentence = str(input("Enter a sentence: "))
    count(sentence)
