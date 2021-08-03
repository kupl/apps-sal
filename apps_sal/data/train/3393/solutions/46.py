import numpy as np
import math


def list_squared(m, n):

    validValues = []

    # cycle through the values
    for testValue in range(m, n):
        divisorList = divisors(testValue)
        totalOfSquareDivisors = sum(np.power(divisorList, 2))               # NumPy again to square all

        # Does result have an even square root? - if so, add to the list
        if (totalOfSquareDivisors % math.sqrt(totalOfSquareDivisors) == 0):
            validValues.append([testValue, totalOfSquareDivisors])

    return validValues

# Use NumPy to determine the valid divisors


def divisors(n):
    r = np.arange(1, int(n ** 0.5) + 1)
    x = r[np.mod(n, r) == 0]
    result = set(np.concatenate((x, n / x), axis=None))
    return [int(i) for i in result]                         # Casts back to integer
