MOD = 10 ** 9 + 7


def ncr(n, r):
    num = den = 1
    for i in range(r):
        num = num * (num - i) % MOD
        den = den * (i + 1) % MOD
    return num * pow(den, MOD - 2, MOD) % MOD


for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = {0: 1}
    for i in a:
        d[i] = 1 if i not in d else d[i] + 1
    ans = 1
    total = 0
    for (i, j) in list(d.items()):
        if i == 0:
            continue
        ans = ans * pow(d[i - 1] if i - 1 in d else 0, j, MOD) % MOD
        total = total + j * (j - 1) // 2
    rem = m - n + 1
    ans = ans * ncr(total, rem) % MOD
    print(ans)
