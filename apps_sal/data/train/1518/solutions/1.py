def isprime(n):
    i = 2
    while i * i < n:
        if n % i == 0:
            return 0
        i += 1
    return 1


def istrue(n, k):
    if n < 2 * k:
        return 0
    if k == 1:
        return isprime(n)
    if k == 2:
        if n % 2 == 0:
            return 1
        return isprime(n - 2)
    return 1


n = int(input())
for i in range(n):
    n, k = list(map(int, input().split()))
    print(istrue(n, k))
