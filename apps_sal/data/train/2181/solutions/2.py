import math

n = int(input())
a = list(map(int, input().split()))
mx = 0
g = [0]*n
r = [0]*n

t1 = [0]*n
t2 = [0]*n

for i in range(n):
	g[i] = max(0, mx-a[i]+1)
	mx = a[i] + g[i]
	t1[i] = mx
	if i > 0:
		g[i] += g[i-1]

mx = 0
for i in range(n-1, -1, -1):
	r[i] = max(0, mx-a[i]+1)
	mx = a[i] + r[i]
	t2[i] = mx
	if i < n-1:
		r[i] += r[i+1]

ans = 10**18
for i in range(n):
	sum = max(t1[i], t2[i]) - a[i];
	if i > 0:
		sum += g[i-1]
	if i < n-1:
		sum += r[i+1]	
	ans = min(ans, sum)	
print(ans)







