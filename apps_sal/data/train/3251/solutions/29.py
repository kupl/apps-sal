import math


def primeFactors(n):
    max = maxPrimeFactors(n)
    facts = []
    for i in range(2, int(max + 1)):
        while n % i == 0:
            facts.append(i)
            n = n / i
    facts_nodup = list(set(facts))
    facts_nodup.sort()
    ret_str = ''
    for x in facts_nodup:
        count = facts.count(x)
        if count > 1:
            ret_str += '({}**{})'.format(x, count)
        else:
            ret_str += '({})'.format(x)
    return ret_str


def maxPrimeFactors(n):
    maxPrime = -1
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i
    if n > 2:
        maxPrime = n
    return int(maxPrime)
