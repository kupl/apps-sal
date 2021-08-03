n, d = (int(x) for x in input().split())
x = [int(x) for x in input().split()]
l = 0
r = 0
ans = 0
while l < n:
    while r < n and x[r] - x[l] <= d:
        r += 1
    ans += (r - l - 1) * (r - l - 2) // 2
    l += 1
print(ans)
