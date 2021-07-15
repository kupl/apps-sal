
from itertools import chain
n = int(input())

a = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    a[i][i] = i

ans = []

while n > 0:
    done = False
    for i in chain(range(1, n-1), [0, n-1]):
        if done:
            break
        b = True
        for dx in -1, 0, 1:
            for dy in -1, 0, 1:
                if dx != 0 and dy != 0:
                    continue
                if dx == 0 and dy == 0:
                    continue
                nx, ny = i+dx, i+dy
                if nx < 0 or nx >= n:
                    continue
                if ny < 0 or ny >= n:
                    continue
                b = b and a[nx][ny] == 1
        if b:
            ans.append(a[i][i])
#            print(ans)
            if i < n - 1:
                a = a[:i] + a[i+1:]
            else:
                a = a[:i]
            for j in range(len(a)):
                if i < n - 1:
                    a[j] = a[j][:i] + a[j][i+1:]
                else:
                    a[j] = a[j][:i]
            for x in range(len(a)):
                for y in range(len(a)):
                    if x == y:
                        continue
                    a[x][y] -= 1
            n -= 1
            done = True
    if not done:
        return
#    for x in a:
#        for y in x:
#            print(y, end = ' ')
#        print()


ret = [0] * len(ans)
for i in range(len(ans)):
    ret[ans[i]] = i + 1

for i in ret:
    print(i, end = ' ')

