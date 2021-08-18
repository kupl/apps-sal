for _ in range(int(input())):
    n, x, m = list(map(int, input().split()))
    l = [int(i) for i in input().split()]
    MOD = 10**9 + 7
    temp = l[:]
    while m:
        for i in range(1, n):
            l[i] = l[i] + l[i - 1]
        m -= 1
    print(l[x - 1] % MOD)
