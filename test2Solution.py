# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

# Execute Python : /usr/bin/python3
# Execute File: /usr/bin/python3  pathOfTheFile

from math import factorial
from sys import argv
import itertools
import functools


# *********************** Test 2 Solution  **************************

# Declaring the list

listOfNumbers = [29, 18, 6, 25, 5, 15, 19, 3, 45, 2]


# Method to get the numbers who are divisor of other number in the list.

def getNumbersAndTheDivisors():
    listOfDivisor = []
    print("1. Get the numbers who are divisor of other number in the list.")
    for index, element in enumerate(listOfNumbers):
        listOfDivisor.clear()
        for index2, element2 in enumerate(listOfNumbers):
            if((element % element2 == 0) and (element2 != element)):
                listOfDivisor.append(element2)
        print(" The divisors of "+str(element) + " are: "+str(listOfDivisor))


# Method to count how many dividend has a divisor

def countHowManyDividenHasAdivisor():
    listOfDividen = []
    print("2. The count of how many dividend has a divisor.")
    for index, element in enumerate(listOfNumbers):
        listOfDividen.clear()
        for index2, element2 in enumerate(listOfNumbers):
            if((element2 % element == 0) and (element2 != element)):
                listOfDividen.append(element2)
        print(" The divisors "+str(element) +
              " has: "+str(len(listOfDividen))+" dividens")


# Method to make a custom sort of the elements


def sortListByEvenOddElement(elem1, elem2):
    evenElem1 = False
    evenElem2 = False
    if(elem1 % 2 == 0):
        evenElem1 = True
    if(elem2 % 2 == 0):
        evenElem2 = True
    if((evenElem1 is True) and (evenElem2 is True)):
        if(elem1 > elem2):
            return -1
        else:
            return -2
    else:
        if((evenElem1 is False) and (evenElem2 is False)):
            if(elem1 > elem2):
                return 0
            else:
                return 1
        else:
            if((evenElem1 is True) and (evenElem2 is False)):
                return -1
            else:
                return 0


# Method to Sort the list putting first even and then odd numbers.

def sortTheListEvenOdd():
    print("3. Sort the list putting first even and then odd numbers.")
    listOfNumbers.sort(reverse=True)
    listOfNumbers.sort(key=functools.cmp_to_key(sortListByEvenOddElement))
    print(" The list sorted is "+str(listOfNumbers))


print("---")
print("The list of numbers is "+str(listOfNumbers))
print("---")
getNumbersAndTheDivisors()
print("---")
countHowManyDividenHasAdivisor()
print("---")
sortTheListEvenOdd()
