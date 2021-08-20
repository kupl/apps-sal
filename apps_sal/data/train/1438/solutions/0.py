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


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    s = []
    for i in range(n):
        s.append(sum(prime_factors(a[i])))
    for i in range(n):
        for j in range(n):
            if i != j and a[j] % a[i] == 0 and (s[j] % s[i] == 0):
                ans = ans + 1
    print(ans)
