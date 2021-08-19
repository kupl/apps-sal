# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    d = dict()
    for i in range(n):
        x, y = input().split()
        y = int(y)
        if x not in d:
            d[x] = [0, 0]
        d[x][y] += 1
    res = 0
    for i in d:
        res += max(d[i])
    print(res)
