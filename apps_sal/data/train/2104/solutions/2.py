n = int(input())
a = []
a = input().split()
for i in range(len(a)):
  a[i] = int(a[i])
a.sort()
c = 0
ans = (a[n - 1]-a[0])*(a[2*n-1]-a[n])
for i in range(n):
  ans = min(ans, (a[i+n-1]-a[i])*(a[2*n-1]-a[0]))
print(ans)

