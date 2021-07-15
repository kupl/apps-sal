n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
now = x[0]
for xx in x[1:]:
    ans += min((xx-now)*a, b)
    now = xx

print(ans)
