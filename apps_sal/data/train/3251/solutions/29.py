import math


def primeFactors(n):
    # returns the maximum prime factor
    max = maxPrimeFactors(n)

    # factorize n and stores factors in facts
    facts = []
    for i in range(2, int(max + 1)):
        while n % i == 0:
            facts.append(i)
            n = n / i

    # removes duplicates for ret and sorts the list
    facts_nodup = list(set(facts))
    facts_nodup.sort()
    # formats return string
    ret_str = ""
    for x in facts_nodup:
        count = facts.count(x)
        if count > 1:
            ret_str += "({}**{})".format(x, count)
        else:
            ret_str += "({})".format(x)

    return ret_str

# A function to find largest prime factor


def maxPrimeFactors(n):

    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2

    # n must be odd at this point,
    # thus skip the even numbers and
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

    # This condition is to handle the
    # case when n is a prime number
    # greater than 2
    if n > 2:
        maxPrime = n

    return int(maxPrime)
