import math
t = eval(input())
while t > 0:
    (n, m) = list(map(int, input().split()))
    f = []
    (min_x, max_x, min_y, max_y) = (1001, -1, 1001, -1)
    for x in range(n):
        f.append(input().strip())
    for i in range(n):
        for j in range(m):
            if f[i][j] == '*':
                if min_x > i:
                    min_x = i
                if max_x < i:
                    max_x = i
                if min_y > j:
                    min_y = j
                if max_y < j:
                    max_y = j
    if max_x == -1 or min_x == 1001 or max_y == -1 or (max_y == 1001):
        print(0)
    else:
        dx = max_x - min_x
        dy = max_y - min_y
        res = 0
        if dx > dy:
            res = int(math.ceil(dx / 2.0)) + 1
        else:
            res = int(math.ceil(dy / 2.0)) + 1
        if res > 0:
            print(res)
        else:
            print(res)
    t -= 1
