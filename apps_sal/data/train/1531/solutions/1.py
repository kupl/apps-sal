N = int(input())
a = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    t = x - 1
    if(t - 1 >= 0):
        a[t - 1] = a[t - 1] + (y - 1)
    if(t + 1 <= N - 1):
        a[t + 1] = a[t + 1] + (a[t] - y)
    a[t] = 0


for j in a:
    print(j)
