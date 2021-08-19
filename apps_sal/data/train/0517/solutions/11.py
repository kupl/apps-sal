def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


(n, m) = map(int, input().split())
fs = prime_factors(n)
ans = 2 ** n - 2
for v in fs:
    if v != n:
        ans -= 2 ** v - 2
print(ans % m)
