"""
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.
"""

#a Fibonacci sequence is a sequence where the current number is the sum of two preceding numbers


def fibonacci():
    secondPreceding = 0
    firstPreceding = 1
    while firstPreceding + secondPreceding <= 100:
        currentTerm = firstPreceding + secondPreceding
        print(currentTerm,",")
        secondPreceding = firstPreceding
        firstPreceding = currentTerm

fibonacci() 

