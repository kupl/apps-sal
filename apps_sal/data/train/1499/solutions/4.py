# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())

    ml = []
    for i in range(n):
        ml.append(list(map(int, input().split())))
    s = input()
    p, q = map(int, input().split())
    nl = [0] * (n + m - 1)
    pl = [0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            if ml[i][j] != int(s[i + j]):
                nl[i + j] += 1
            else:
                pl[i + j] += 1
    c = 0
    for i in range(len(nl)):
        c += min(nl[i] * p, pl[i] * p + q)
    print(c)
