def count_find_num(primesL, n):
    base = 1
    for p in primesL:
        base *= p
    arr = permPrime(base, primesL, n)
    if len(arr) == 0:
        return []
    return [len(arr), max(arr)]


def permPrime(base, primesL, n):
    if base > n:
        return []
    arr = [base]
    for p in primesL:
        arr += permPrime(base * p, primesL, n)
    arr = list(set(arr))
    return arr
