import sys
read = sys.stdin.readline
n = int(read())
a = list(map(int, read().split()))
b = [i for i in a]
boola = [False for i in range(n)]
for i in range(2, n):
    a[i] += min(a[i - 1], a[i - 2])
b.reverse()
for i in range(2, n):
    b[i] += min(b[i - 1], b[i - 2])
print(min(a[-1], b[-1]))
