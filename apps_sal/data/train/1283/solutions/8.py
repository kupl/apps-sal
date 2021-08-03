def sievearray():
    n = 200
    sieve = [1 for i in range(n + 1)]
    sieve[0] = 0
    sieve[1] = 0
    i = 2
    while i * i <= n:
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
        i += 1
    return sieve


def semiprime(n):
    i = 2
    m2 = 0
    m1 = 0
    while i != n:
        if n % i == 0 and sieve[i] == 1:
            m1 = i
        if n == m1 * m2 and m1 != m2:
            return 1
        else:
            m2 = m1
            i += 1
    return 0


def sum_of_two(n):
    for i in range(2, n // 2 + 1):
        p = i
        q = n - i
        if semiprime(p) and semiprime(q):
            return 1


try:
    t = 0
    t = int(input())
    sieve = sievearray()
except Exception:
    pass
l1 = [0 for i in range(0, t)]
for i in range(0, t):
    l1[i] = int(input())
for i in range(0, len(l1)):
    if sum_of_two(l1[i]):
        print("YES")
    else:
        print("NO")
