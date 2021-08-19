from numpy import arange


def divisors(integer):
    potential_divisors = arange(2, integer // 2 + 1)
    divisors = potential_divisors[integer % potential_divisors == 0]
    if len(divisors):
        return list(divisors)
    else:
        return '{integer} is prime'.format(integer=integer)
