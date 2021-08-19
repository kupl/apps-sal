def offset(l, flag):
    x = 0
    for i in range(1, len(l)):
        temp = []
        for j in range(i):
            v = getbig(l[i], l[j], fs)
            if v > 1:
                temp.append(v)
                if flag:
                    x += 2 ** v - 2
                else:
                    x -= 2 ** v - 2
        x += offset(temp, not flag)
    return x


def getbig(v1, v2, factors):
    x = 1
    for f in factors:
        while v1 % f == 0 and v2 % f == 0:
            v1 //= f
            v2 //= f
            x *= f
    return x


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
if n == 1:
    print(1)
else:
    fs = prime_factors(n)
    fs.discard(n)
    ans = 2 ** n - 2
    temp = []
    for v in fs:
        v = n // v
        temp.append(v)
        ans -= 2 ** v - 2
    ans += offset(temp, True)
    print(ans % m)
