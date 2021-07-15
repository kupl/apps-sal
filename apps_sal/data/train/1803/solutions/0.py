from collections import Counter
from itertools import combinations
from operator import mul
from functools import reduce

def largest_palindrom_from(n):
    digits = sorted(str(n))
    singles, pairs = [], []
    
    # group digits to pairs and singles
    while digits:
        digit = digits.pop()
        if digits and digit == digits[-1]:
            pairs.append(digit)
            digits.pop()
        else:
            singles.append(digit)
    
    # avoid trailing zeros
    if pairs and pairs[0] == '0':
        pairs = []
    
    # return largest possible palindrom
    if not singles:
        singles = ['']
    return int( ''.join(pairs) + singles[0] + ''.join(pairs[::-1]) )


def numeric_palindrome(*args):
    args = Counter(args)
    candidates = set()
    
    # remove extra 0s and 1s
    for n in [0, 1]:
        if args[n] > 2:
            args[n] = 2
    
    args = list(args.elements())
    
    # check all possible products
    for n in range(2, len(args)+1):
        for combo in combinations(args, n):
            product = reduce(mul, combo)
            candidates.add( largest_palindrom_from(product) )
    
    return max(candidates)
