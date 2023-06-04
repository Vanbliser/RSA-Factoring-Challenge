#!/usr/bin/python3
import math
import sys

def perfect_square(n):
    """function to check if n is a perfect square
    Args:
        n (int): number to check
    Returns:
        return True if it's a prime number, else False
    """
    sq_root = int(math.sqrt(n))
    return (sq_root*sq_root) == n


if len(sys.argv) != 2:
    sys.exit(1)

filename = sys.argv[1]
try:
    with open(filename, "r") as file:
        for lines in file.readlines():
            number = int(lines)
            x = math.ceil(math.sqrt(number))
            while not perfect_square((x**2) - number):
                x += 1
            y = math.sqrt((x**2) - number)
            print(f"{number}={int(abs(x-y))}*{int(abs(x+y))}")
except FileNotFoundError:
    sys.exit(1) 
