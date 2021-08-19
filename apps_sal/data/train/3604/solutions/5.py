from bisect import bisect
LIMIT = 1 + 300000
happySieve = [None] * LIMIT
happySieve[1] = 1


def happyOnes(n):
    seen = set()
    while 1:
        if happySieve[n] is not None:
            return (happySieve[n], seen)
        if n in seen or n == 1:
            return (n == 1, seen)
        seen.add(n)
        n = sum((int(d) ** 2 for d in str(n)))


for n in range(1, LIMIT):
    (isH, seen) = happyOnes(n)
    for x in seen:
        happySieve[x] = isH
HAPPY = [i for i in range(1, LIMIT) if happySieve[i]]


def performant_numbers(n):
    return HAPPY[:bisect(HAPPY, n)]
