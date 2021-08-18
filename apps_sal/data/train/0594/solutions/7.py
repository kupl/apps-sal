n, x = list(map(int, input().split()))
l = list(map(int, input().split()))
res = l[0]
temp = l[0]
for i in range(1, n):
    temp = max(l[i], temp + l[i])
    res = max(temp, res)
print(sum(l) - res + (res / x))
