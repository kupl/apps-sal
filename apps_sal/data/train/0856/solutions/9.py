for _ in range(int(input())):
    n = int(input())
    d = dict()
    for i in range(n):
        x, y = input().split()
        y = int(y)
        if x not in d:
            d[x] = [0, 0]
        d[x][y] += 1
    ans = 0
    for i in d:
        ans += max(d[i])

    print(ans)
