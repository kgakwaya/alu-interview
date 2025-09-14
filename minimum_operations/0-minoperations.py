
dule for calculating minimum operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to get exactly n H characters in the file.
    If n is impossible to achieve, return 0.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

