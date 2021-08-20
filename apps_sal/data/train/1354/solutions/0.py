A = [0] * 100001
M = 1000000007


def nCk(n, k):
    if k == 0 or k == n:
        return 1
    r = A[n - k] * A[k] % M
    x = A[n] * pow(r, M - 2, M) % M
    return x


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    for i in range(n - 1):
        (u, v) = input().split()
    summ = 0
    A[0] = 1
    for i in range(1, len(A)):
        A[i] = i * A[i - 1] % M
    for i in range(min(n, k)):
        b = nCk(k, i + 1)
        c = nCk(n - 1, i) * b % M
        c *= A[i + 1]
        summ += c % M
        summ %= M
    print(summ)
