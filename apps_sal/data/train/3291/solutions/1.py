limit = 10_000
sieve = [0] * 2 + list(range(2, limit))
for i in range(2, limit):
    for j in range(i * i, limit, i):
        sieve[j] = 0

primes = {i for i in sieve if i}


def primes_a_p(l, u):
    li, found = sorted([i for i in primes if l <= i <= u]), []

    for i, a in enumerate(li):
        for b in li[i + 1:]:
            diff, tray = b - a, [a, b]

            for _ in range(4):
                c = tray[-1] + diff
                if c in primes and c < u:
                    tray.append(c)
                    continue
                break

            if len(tray) == 6:
                found.append(tray)

    return found
