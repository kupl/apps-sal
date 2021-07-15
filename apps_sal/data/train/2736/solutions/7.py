from itertools import permutations
from collections import defaultdict

def find_largest(lst):
    candidates = map("".join, permutations(lst))
    return max(candidates)

def largest_arrangement(numbers):
    first_digit = defaultdict(list)
    
    for n in map(str, numbers):
        first_digit[n[0]].append(n)
    
    result = "".join(find_largest(first_digit[d]) for d in "9876543210")
    return int(result)
