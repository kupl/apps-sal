ans = [[False for _ in range(1000)] for _ in range(1000)]
for _ in range(int(input())):
    (r, c) = map(int, input().split())
    count = 0
    for i in range(0, r * c):
        val = 0
        for x in range(0, r * c, i + 1):
            a = x // r
            b = x % r
            if not ans[a][b]:
                ans[a][b] = True
                val += 1
            a = x % c
            b = x // c
            if not ans[a][b]:
                ans[a][b] = True
                val += 1
        for x in range(0, r * c, i + 1):
            a = x // r
            b = x % r
            ans[a][b] = False
            a = x % c
            b = x // c
            ans[a][b] = False
        print(val, end=' ')
