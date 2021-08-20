(n, m) = list(map(int, input().split()))
l = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    l[i] += x
t = int(input())
for _ in range(t):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    vol = 0
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            vol += l[i][j]
    print(vol)
