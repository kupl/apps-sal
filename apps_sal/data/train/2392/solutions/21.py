def mi():
    return list(map(int, input().split()))


'''
7
1 1
10 1
100 3
1024 14
998244353 1337
123 144
1234312817382646 13
1
45
153
294
3359835
0
427262129093995
'''
for _ in range(int(input())):
    n, m = mi()
    lpage = n - n % m
    lmul = lpage // m
    fpage = m
    fmul = 1
    if n < m:
        print(0)
        continue
    c = []
    for i in range(1, 100):
        cons = (i * m) % 10
        if not len(c):
            c.append(cons)
        elif c[0] != cons:
            c.append(cons)
        else:
            break
    nmul = lmul - fmul + 1
    print(sum(c) * (nmul // len(c)) + sum(c[:nmul % len(c)]))
