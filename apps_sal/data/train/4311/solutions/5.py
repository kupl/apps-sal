import math
import itertools

def is_prime(num):
    return num > 1 and all(num % i for i in range(2, num if num < 53 else math.ceil(math.sqrt(num)) + 1))

def solve(a,b):
    return len([cb for cb in itertools.combinations_with_replacement([i for i in range(a, b) if is_prime(i)], 2) if is_prime(sum([int(c) for c in str(cb[0] * cb[1])]))])
