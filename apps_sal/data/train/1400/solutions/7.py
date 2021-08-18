for _ in range(int(input())):
    n, l, r = [int(x) for x in input().split()]
    s1, s2 = [1] * n, []
    l -= 1
    x = 2
    for _ in range(l):
        s1[_] = x
        x = x * 2
    x1 = sum(s1)
    s = 1
    for _ in range(r):
        s2.append(s)
        s = s * 2
    s = s // 2
    for _ in range(r, n):
        s2.append(s)
    x2 = sum(s2)
    print(x1, x2)
