from sys import stdin, stdout


def isprime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return 0
        i += 1
    return 1


def isSum(N, K):
    if N < 2 * K:
        return 0
    if K == 1:
        return isprime(N)
    if K == 2:
        if N % 2 == 0:
            return 1
        return isprime(N - 2)
    return 1


test = int(stdin.readline())
for _ in range(test):
    (n, k) = map(int, stdin.readline().split())
    if isSum(n, k):
        stdout.write('1' + '\n')
    else:
        stdout.write('0' + '\n')
