N = 50000
sieve, reduceable = [False, False] + [True] * (N - 1), set()
for i, is_prime in enumerate(sieve):
    if is_prime:
        seen, n = set(), i
        while n not in seen:
            seen.add(n)
            n = sum(int(c)**2 for c in str(n))
            if n == 1:
                reduceable.add(i)

        for j in range(i * i, N + 1, i):
            sieve[j] = False


def solve(a, b):
    return sum(1 for e in reduceable if a <= e < b)
