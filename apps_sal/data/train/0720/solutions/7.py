# cook your dish here
from sys import stdin


def sin():
    return stdin.readline()


def ans(s):
    c = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            d = s[i:j + 1]
            a = d.count("0")
            b = d.count("1")
            if a == b * b:
                c += 1
    return(c)


test = int(sin())
for _ in range(test):
    s = input()
    x = 1
    ans = 0
    n = len(s)
    te = [0] * (n + 1)
    for i in range(1, n + 1):
        te[i] += (te[i - 1] + int(s[i - 1]))
    ps = te[0]
    l = x * x + x
    while l <= n:
        i = 0
        while i <= n - l:
            j = i + l
            cnt1 = te[j] - te[i]
            if cnt1 == x:
                ans += 1
                i += 1
            else:
                i += abs(x - cnt1)
        x += 1
        l = x * x + x
    print(ans)
