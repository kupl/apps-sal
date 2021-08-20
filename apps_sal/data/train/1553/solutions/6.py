from numpy import *
(m, n) = list(map(int, input().split()))
trees = array([[None] * n] * m)
for i in range(m):
    trees[i] = list(map(int, input().split()))
c = int(input())
result = []
for _ in range(c):
    ans = 0
    (x1, y1, x2, y2) = list(map(int, input().split()))
    for i in range(x1 - 1, x2):
        temp = [trees[i, j] for j in range(y1 - 1, y2)]
        ans += sum(temp)
    result.append(ans)
for i in result:
    print(i)
