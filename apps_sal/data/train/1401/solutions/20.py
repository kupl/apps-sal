n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = a[0]
i = 0
while ans <= k and i < n:
 ans += a[i+1]
 i += 1
print(i)
