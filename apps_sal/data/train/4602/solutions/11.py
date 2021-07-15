from operator import eq
from collections import Counter

def is_anagram(test, original):
    return eq(*map(Counter, map(str.lower, (test, original))))
