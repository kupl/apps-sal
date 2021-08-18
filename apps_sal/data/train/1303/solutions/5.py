t = int(input())
MOD = 10**9 + 7
for _ in range(t):
    n, k, m = list(map(int, input().split()))
    b = [0 for i in range(k)]
    a = list(map(int, input().split()))
    if(m == 1):
        for i in range(n):
            for j in range(k - 1, -1, -1):
                if(j == 0):
                    b[j] = (b[j] + 1) % MOD
                else:
                    b[j] = (b[j - 1] + b[j]) % MOD
    else:
        for val in a:
            mod = val % m
            if(mod == 0):
                mod = m
            for j in range(mod - 1, k, m):
                if(j == 0):
                    b[j] = (b[j] + 1) % MOD
                else:
                    b[j] = (b[j - 1] + b[j]) % MOD
    print(b[-1] % MOD)
