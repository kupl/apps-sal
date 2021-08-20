M = 1000000007


def f(n, r):
    if n == 0:
        return 0
    if r > n / 2:
        r = n - r
    if r == 0:
        return 1
    if r > n:
        return 0
    a = 1
    j = 2
    for i in range(0, r):
        a = a * n
        n = n - 1
        while a % j == 0 and j <= r:
            a = a / j
            j = j + 1
    return a % M


T = int(eval(input()))
for i in range(0, T):
    A = input()
    a = [0 for i in range(0, 26)]
    for letter in A:
        a[ord(letter) - ord('a')] = a[ord(letter) - ord('a')] + 1
    nways = 1
    k = len(A)
    for i in range(0, 26):
        nways = nways * f(k, a[i]) % M
        k = k - a[i]
        if k == 0:
            break
    d2 = 0
    d3 = 0
    d4 = 0
    d211 = 0
    d22 = 0
    for i in range(0, 26):
        for j in range(i + 1, 26):
            d2 = (d2 + a[i] * a[j] % M) % M
            d22 = (d22 + f(a[i], 2) * f(a[j], 2) % M) % M
            for k in range(j + 1, 26):
                d3 = (d3 + a[k] * (a[i] * a[j] % M) % M) % M
                d211 = (d211 + f(a[k], 2) * (a[i] * a[j] % M) % M) % M
                d211 = (d211 + f(a[j], 2) * (a[k] * a[i] % M) % M) % M
                d211 = (d211 + f(a[i], 2) * (a[j] * a[k] % M) % M) % M
                for l in range(k + 1, 26):
                    d4 = (d4 + a[i] * a[j] % M * (a[k] * a[l] % M) % M) % M
    ans = (1 + d2 + d3 * 2 + d4 * 3 + d211 * 2 + d22) % M
    ans = (nways - ans + M) % M
    ans = nways * ans % M
    print(ans)
