from sys import*
input = stdin.readline
n = int(input())
t = []
for i in range(n):
    a, b = list(map(int, input().split()))
    t.append([a, b])
if(n == 1):
    c = 1
else:
    c = 2
for i in range(1, n - 1):
    l = t[i][0] - t[i - 1][0]
    r = t[i + 1][0] - t[i][0]
    h = t[i][1]
    if(h < l):
        c += 1
    elif(h < r):
        c += 1
        t[i][0] = t[i][0] + h
print(c)
