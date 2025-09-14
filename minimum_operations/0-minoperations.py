#!/usr/bin/python3
"""
This module contains a function that calculates the
minimum number of operations needed to obtain exactly
n H characters in a text file, starting with one H.
The only operations allowed are "Copy All" and "Paste".
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations to reach n Hs,
             or 0 if it is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
