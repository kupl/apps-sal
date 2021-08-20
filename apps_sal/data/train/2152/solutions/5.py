from itertools import accumulate


def divisors(n):
    tab = []
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            while n % i == 0:
                n //= i
            tab.append(i)
    if n > 1:
        tab.append(n)
    return tab


n = int(input())
a = list(map(int, input().split()))
s = sum(a)
tab = divisors(s)
if s == 1:
    print(-1)
else:
    m = 10 ** 18
    pref = list(accumulate(a))
    for k in tab:
        x = 0
        for i in range(n - 1):
            x += min(pref[i] % k, k - pref[i] % k)
        m = min(m, x)
    print(m)
