"""
Name: pi.py
Purpose: Get the value of Pi to n number of decimal places
based on:Pradipta (geekpradd) 's program
Author: GuoJia(nmbvd)
Algorithm: Chudnovsky Algorithm
License: MIT
Module Dependencies:
Math provides fast square rooting
Decimal gives the Decimal data type which is much better than Float
sys is needed to set the depth for recursion.
"""
from __future__ import print_function
import math, sys
import sympy
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

python2 = sys.version_info[0] == 2
if python2:
    input = raw_input

def calPi(m):
    getcontext().prec = (m+1)
    sum=Decimal(0)
    for n in range(m+1):
        product = Decimal(1)
        for i in range(1,n+1):
            product*=Decimal(Decimal((5*n+i)/i)*Decimal((4*n+i)/i)*Decimal((3*n+i)/i)/(-640320)**3)
            #print(product)
        sum+=Decimal(product*(13591409 + 545140134 * n))
    pi= Decimal(Decimal((426880 * Decimal(sympy.sqrt(10005))))/sum)
    return pi


def shell():
    """
    Console Function to create the interactive Shell.
    Runs only when __name__ == __main__ that is when the script is being called directly
    No return value and Parameters
    """
    print(
        "Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")

    while True:
        print(">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("You did not enter a number. Try again")
        else:
            print(calPi(int(entry)))

if __name__ == '__main__':
    shell()