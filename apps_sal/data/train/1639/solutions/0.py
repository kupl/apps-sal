import math


def gta(limit, *args):
    return sum_up(limit, make_pattern(limit, *args))


def binomial_coeff(n, k):
    """N choose K"""
    return math.factorial(n) / math.factorial(n - k)


def sum_up(limit, items):
    """
    Basic Idea: 

    The number of cominations is simply N choose K. We calcuate this n-times up to the limit.

    To sum up all the digits we don't have to calculate the sum of each permuation, rather, we simply have to 
    realise that the digit "1" will appear N times.

        For example: [1,2,3], pick = 3.  

        If there are 6 combinations of length 3 for 3 numbers then each number much appear once in each combination. 
        Thus the sum is: (1 * 6) + (2 * 6) + (3 * 6)

        In cases where we have N numbers and need to pick K of them then that means not all numbers appear in all combinations.
        It turns out combinations_total / (N / limit) gives us how many times N appears in the list of all combinations. 

        For example: [1,2,3] pick 2
        [1,2]
        [2,1]
        [1,3]
        [3,1]
        [2,3]
        [3,2]

        We can see that 1 appears 4/6 times. 
        combinations_total = 6, N = 3, limit = 2.

        6 / (3/2) = 4
    """
    total = 0
    for i in range(1, limit + 1):
        combin = binomial_coeff(len(items), i)
        ratio = len(items) / float(i)

        for element in items:
            total += (element * (combin / ratio))

    return total


def make_pattern(limit, *args):

    seen = set()
    pattern = []
    items = list(map(str, args))

    k = 0
    while len(pattern) < limit:
        for i in range(len(items)):
            try:
                v = items[i][k]
            except IndexError:
                pass

            if v not in seen:
                seen.add(v)
                pattern.append(int(v))
                if len(pattern) == limit:
                    break
        k += 1

    return pattern
