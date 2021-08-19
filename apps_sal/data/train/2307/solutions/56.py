(n, a, b) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 0
for i in range(len(x) - 1):
    walk_cost = a * (x[i + 1] - x[i])
    if b < walk_cost:
        ans += b
    else:
        ans += walk_cost
print(ans)
