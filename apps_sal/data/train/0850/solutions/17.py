from math import gcd
for _ in range(int(input())):
    input()
    li = sorted(list(set(list(int(i) for i in input().split()))))
    if len(li) == 1:
        print(2 * li[0])
    elif len(li) == 2:
        print(sum(li))
    else:
        g = li[0]
        for i in range(1, len(li) - 2):
            g = gcd(li[i], g)
        m = gcd(g, li[-2]) + li[-1]
        n = gcd(g, li[-1]) + li[-2]
        print(max(m, n))
