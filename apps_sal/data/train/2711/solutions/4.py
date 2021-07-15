from itertools import product

def outcome(n, s, k):
    return sum(1 for roll in product(range(1, s + 1), repeat=n) if sum(roll) == k) 
