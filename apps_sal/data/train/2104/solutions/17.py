n = int(input())
a = list(map(int, input().split()))
a.sort()
x = float('Inf')
for i in range(1, n):
    x = min(x, a[i + n - 1] - a[i])
print(min((a[n - 1] - a[0]) * (a[-1] - a[n]), x * (a[-1] - a[0])))
