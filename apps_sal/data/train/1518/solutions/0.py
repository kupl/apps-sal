from math import sqrt


def isprime(n):
    if n % 2 == 0 and n > 2 or n == 1:
        return 0
    else:
        s = int(sqrt(n)) + 1
        for i in range(3, s, 2):
            if n % i == 0:
                return 0
        return 1


def find(N, K):
    if N < 2 * K:
        return 0
    if K == 1:
        return isprime(N)
    if K == 2:
        if N % 2 == 0:
            return 1
        return isprime(N - 2)
    return 1


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    print(find(n, k))
