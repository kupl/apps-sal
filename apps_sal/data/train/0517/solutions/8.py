def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(n)
            if n % i != 0:
                factors.add(i)
            break
    return factors


(n, m) = map(int, input().split())
if n > 1:
    fs = prime_factors(n)
    ans = 2 ** n - 2
    for v in fs:
        ans -= 2 ** v - 2
    print(ans % m)
else:
    print(1)
