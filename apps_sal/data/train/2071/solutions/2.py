n = int(input())
l = []
for i in range(n):
	a,b = map(int,input().split())
	l.append((a,b))

def solve(a):
	ans, d = 0, {}
	for x,_ in a:
		d[x] = d.setdefault(x,0)+1
	for i in d:
		ans += d[i]*(d[i]-1) // 2
	return ans

x = 0
pd = {}
for i in l:
	pd[i] = pd.setdefault(i,0)+1
for i in pd:
	x += pd[i]*(pd[i]-1) // 2

y = solve(l)
z = solve([(p,q) for q,p in l])
print(y+z-x)
