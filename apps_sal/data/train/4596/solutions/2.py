from collections import Counter
import math


def perms(element):
    stringElement = str(element)
    tally = Counter(stringElement)
    topPart = math.factorial(len(stringElement))
    product = 1
    for t in tally:
        product = product * math.factorial(tally[t])
    return topPart / product
