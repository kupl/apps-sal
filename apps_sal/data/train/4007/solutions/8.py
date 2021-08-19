from functools import reduce


def gcd(a, b):
    return gcd(b, a % b) if b else a


def finding_k(arr):
    return reduce(lambda a, b: gcd(a, b), [abs(e - arr[0]) for e in arr]) or -1
