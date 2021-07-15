import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	n, dc = mints()
	a = list(mints())
	a.append(0)
	x = [0]*n
	y = [0]*n
	for i in range(n):
		x[i], y[i] = mints()
	d = [1<<30]*n
	d[0] = 0
	was = [False]*n
	for i in range(n):
		m = 1<<30
		mi = 0
		for j in range(n):
			if not was[j] and m > d[j]:
				m = d[j]
				mi = j
		j = mi
		was[j] = True
		for k in range(n):
			if not was[k]:
				dd = d[j] + (abs(x[k]-x[j])+abs(y[k]-y[j]))*dc
				dd -= a[k-1]
				if d[k] > dd:
					d[k] = dd
	print(d[-1])

solve()

