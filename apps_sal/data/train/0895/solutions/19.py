import sys
read = sys.stdin.readline
n = int(read())
a = list(map(int, read().split()))
b = [i for i in a]
boola = [False for i in range(n)]
#ans = 0
for i in range(2, n):
    a[i] += min(a[i - 1], a[i - 2])
# print(*boola)
b.reverse()
for i in range(2, n):
    b[i] += min(b[i - 1], b[i - 2])
#x = min(a[-1],a[-2])
#y = min(b[-1],b[-2])
print(min(a[-1], b[-1]))
