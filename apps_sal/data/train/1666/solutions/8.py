def gcd(x, y):
    if x < y:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x


def solution(arr):
    uniques = list(set(arr))
    N = len(arr)
    if N < 2 or len(uniques) == 1:
        return arr[0] * N

    min_gcd = gcd(uniques[0], uniques[1])
    for i in range(2, len(uniques)):
        if min_gcd == 1:
            return N
        cur = gcd(min_gcd, uniques[i])
        min_gcd = min(cur, min_gcd)

    return min_gcd * N
