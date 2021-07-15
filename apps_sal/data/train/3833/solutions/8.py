import itertools
def longest(s1, s2):
    longest = ""
    for i in s1: 
        if i not in longest:
            longest += i
    for i in s2:
       if i not in longest:
            longest += i 
    return ''.join(sorted(longest))
