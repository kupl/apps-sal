def not_prime(x):
    if x == 1: return True
    for y in range(2, int(x ** 0.5) + 1):
        if x % y == 0:
            return True
    return False
def odd_not_prime(n):
    return sum(not_prime(x) for x in range(1, n + 1, 2))
