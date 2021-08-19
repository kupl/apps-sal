import sys
input = sys.stdin.readline
n = int(input())
x = []
y = []
for i in range(n):
    (xi, yi) = map(int, input().split())
    x.append(xi)
    y.append(yi)
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)
answer = 0
for i in range(n):
    dx = max(max_x - x[i], x[i] - min_x)
    dy = max(max_y - y[i], y[i] - min_y)
    answer = max(answer, dx + dy)
print(2 * answer, end=' ')
for i in range(4, n + 1):
    print(2 * (max_x - min_x + max_y - min_y), end=' ')
