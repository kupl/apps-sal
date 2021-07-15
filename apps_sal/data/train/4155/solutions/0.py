REV = {'6':'9', '9':'6'}
BASE = set("01869")

def isReversible(n):
    s = str(n)
    return ( not (set(s) - BASE)                                                          # contains only reversible characters
             and (not len(s)%2 or s[len(s)//2] not in "69")                               # does not contain 6 or 9 right in the middle (only for odd number of digits)
             and all( REV.get(c, c) == s[-1-i] for i,c in enumerate(s[:len(s)//2]) ))     # symmetric repartition

def solve(a, b):
    return sum( isReversible(n) for n in range(a,b) )
