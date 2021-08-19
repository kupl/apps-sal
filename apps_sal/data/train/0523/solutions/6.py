MOD = 10 ** 9 + 7


def binomialCoefficient(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return int(res)


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    value = binomialCoefficient(n - 1, k - 1)
    ans = 1
    for x in range(1, n - 1):
        if n - x - 1 >= k - 1:
            temp1 = binomialCoefficient(n - x - 1, k - 1)
        else:
            temp1 = 0
        if x >= k - 1:
            temp2 = binomialCoefficient(x, k - 1)
        else:
            temp2 = 0
        ans = ans * arr[x] ** (value - temp2 - temp1) % MOD
    print(ans)
