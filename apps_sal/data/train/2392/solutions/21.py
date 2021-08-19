def mi():
    return list(map(int, input().split()))


'\n7\n1 1\n10 1\n100 3\n1024 14\n998244353 1337\n123 144\n1234312817382646 13\n1\n45\n153\n294\n3359835\n0\n427262129093995\n'
for _ in range(int(input())):
    (n, m) = mi()
    lpage = n - n % m
    lmul = lpage // m
    fpage = m
    fmul = 1
    if n < m:
        print(0)
        continue
    c = []
    for i in range(1, 100):
        cons = i * m % 10
        if not len(c):
            c.append(cons)
        elif c[0] != cons:
            c.append(cons)
        else:
            break
    nmul = lmul - fmul + 1
    print(sum(c) * (nmul // len(c)) + sum(c[:nmul % len(c)]))
