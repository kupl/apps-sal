from collections import Counter
from functools import reduce
from math import gcd


def has_subpattern(string):  
    chars_frequency = Counter(string)
    greatercd = reduce(gcd, chars_frequency.values())
    charslist = sorted(chars_frequency.items())
    pattern = ""
    for char, frequency in charslist:
        pattern += char * (frequency // greatercd)
    return pattern
