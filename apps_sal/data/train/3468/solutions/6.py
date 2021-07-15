from collections import Counter
from operator import sub

def scramble(s1,s2):
    return not sub(*map(Counter, (s2,s1)))
