from bisect import bisect
sieve = [None] * 300001


def is_happy(n):
    seen = set()
    while True:
        if sieve[n] is not None:
            return (sieve[n], seen)
        if n == 1:
            break
        elif n < 7:
            return (False, seen)
        seen.add(n)
        n = sum((int(x) ** 2 for x in str(n)))
    return (True, seen)


for i in range(1, 300000 + 1):
    (state, seen) = is_happy(i)
    for x in seen:
        sieve[x] = state
FINAL = [1] + [idx for idx in range(1, 300001) if sieve[idx]]


def performant_numbers(n):
    first = 0
    last = len(FINAL) - 1
    idx = float('inf')
    while first <= last:
        mid = (first + last) // 2
        if n == FINAL[mid]:
            idx = mid + 1
            break
        elif n < FINAL[mid]:
            idx = mid
            last = mid - 1
        else:
            first = mid + 1
    return FINAL[:idx]
