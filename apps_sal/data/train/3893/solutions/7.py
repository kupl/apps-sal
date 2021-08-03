from numpy import arange


def divisors(integer):
    # generate array of integers from 2 to integer/2 (rounded down)
    potential_divisors = arange(2, integer // 2 + 1)
    # use boolean indexing to extract divisors
    divisors = potential_divisors[integer % potential_divisors == 0]
    # check divisors exist and if not return prime message
    if len(divisors):
        return list(divisors)
    else:
        return '{integer} is prime'.format(integer=integer)
