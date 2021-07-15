n, a, b = map(int, input().split())
x = list(map(int, input().split()))
x = [(x[i] - x[i-1])*a for i in range(1, n)]
res = 0
for xi in x:
    if xi > b:
        res += b
    else:
        res += xi
print(res)
