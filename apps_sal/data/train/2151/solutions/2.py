n, s = list(map(int, input().split()))

a = list(map(int, input().split()))

a.sort()

m = n // 2

ans = 0

if a[m] > s:
    ans = sum([max(x - s, 0) for x in a[:m+1]])
if a[m] < s:
    ans = sum([max(s - x, 0) for x in a[m:]])

print(ans)

