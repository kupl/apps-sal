n, a, b = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

ans = 0
tmp = x[0]

for i in x[1:]:
    ans += min((i - tmp) * a, b)
    tmp = i

print(ans)
