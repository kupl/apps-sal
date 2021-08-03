# generate happy numbers up to LIMIT
from bisect import bisect
LIMIT = 300000
HAPPY, SAD = set(), set()

for n in range(1, LIMIT + 1):
    seen = set()
    while True:
        seen.add(n)
        n = sum(d * d for d in map(int, str(n)))

        if n == 1 or n in HAPPY:
            HAPPY |= seen
            break
        elif n in seen or n in SAD:
            SAD |= seen
            break

HAPPY = sorted(HAPPY)


def performant_numbers(n):
    return HAPPY[:bisect(HAPPY, n)]
