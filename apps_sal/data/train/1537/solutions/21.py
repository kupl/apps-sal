def primes_sieve(limit):
    limitn = limit + 1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i * 2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes


l = 1000000007
p = primes_sieve(81043)
s = []
i = 0
while p[i] < len(p) - 1:
    s.append(p[p[i] - 1])
    i += 1
b = [s[0]]
for i in range(1, len(s)):
    b.append(b[len(b) - 1] + s[i])
for _ in range(int(input())):
    n = int(input())
    print(b[n - 1])
