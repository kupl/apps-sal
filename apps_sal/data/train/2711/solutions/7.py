from itertools import product
def outcome(n, s, k):
    return sum(sum(x) == k for x in product(range(1, s + 1), repeat=n))
