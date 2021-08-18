MOD = (10**9) + 7


def binomialCoefficient(n, r, p):

    C = [0 for i in range(r + 1)]

    C[0] = 1

    for i in range(1, n + 1):

        for j in range(min(i, r), 0, -1):

            C[j] = (C[j] + C[j - 1]) % p

    return int(C[r])


for _ in range(int(input())):

    n, k = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    value = binomialCoefficient(n - 1, k - 1, MOD)

    ans = 1

    for x in range(1, n - 1):

        if (n - x - 1) >= (k - 1):

            temp1 = binomialCoefficient(n - x - 1, k - 1, MOD)
        else:
            temp1 = 0

        if x >= (k - 1):

            temp2 = binomialCoefficient(x, k - 1, MOD)
        else:
            temp2 = 0

        ans = (ans * (arr[x]**(value - temp2 - temp1))) % MOD

    print(ans)
