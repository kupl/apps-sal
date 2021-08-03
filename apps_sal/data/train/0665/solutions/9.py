import math

try:
    for _ in range(int(input())):
        n, m = list(map(int, input().split()))
        p = list(map(int, input().split()))
        points = [[0 for i in range(m + 1)]for i in range(n)]
        for i in range(n):
            points[i][0] = p[i]
        mx = [[0, 0] for i in range(n)]
        arr = [[3000, 0] for i in range(n)]
        for i in range(n):
            lst = list(map(int, input().split()))
            for j in range(1, m + 1):
                points[i][j] = points[i][j - 1] + lst[j - 1]
            points[i] = points[i][1:]
            arr[i][1] = points[i][0]
        for i in range(m):
            rank = []
            for j in range(n):
                rank.append(points[j][i])
            rank = sorted(rank, reverse=True)
            for j in range(n):
                pos = rank.index(points[j][i])
                if(pos < arr[j][0]):
                    mx[j][1] = i
                    arr[j][0] = pos
            for j in range(n):
                if(points[j][i] > arr[j][1]):
                    mx[j][0] = i
                    arr[j][1] = points[j][i]
        ans = 0
        for x in mx:
            if(x[0] != x[1]):
                ans += 1
        print(ans)
except EOFError as e:
    pass
