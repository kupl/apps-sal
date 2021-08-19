from collections import Counter
from collections import defaultdict
p = 10 ** 5 + 5


def Sieve():
    l = [True] * p
    s = [0] * p
    for i in range(2, p):
        if l[i]:
            for j in range(i, p, i):
                s[j] += i
                l[j] = False
        i += 1
    l[0] = l[1] = False
    return (l, s)


(isprime, s) = Sieve()
good = defaultdict(list)
for i in range(2, p):
    for j in range(i, p, i):
        if s[j] % s[i] == 0:
            good[i].append(j)
for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    c = Counter(l)
    ans = 0
    for i in range(2, p):
        if c[i]:
            for j in good[i]:
                ans += c[i] * c[j]
    ans -= n
    print(ans)
