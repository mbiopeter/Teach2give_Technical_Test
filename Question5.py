"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit 
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""

def reverse_int(integer):
    numberString = str(integer)
    if numberString[0] == "-":
        reversedNum = "-" + numberString[:0:-1]
        return reversedNum
    else:
        reversedNum = numberString[::-1]
        return reversedNum


while True:
    integer = int(input("Enter an integer: "))
    reverse_int(integer)