import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline());
	v = list(map(int,sys.stdin.readline().split()))
	v.sort()
	xm,cm = v[0],0
	x,c = v[0],0
	for i in v:
		if i == x:
			c += 1
		else:
			if c > cm or (c == cm and x < xm):
				xm,cm = x,c
			x, c = i, 1
	if c > cm or (c == cm and x < xm):
		xm,cm = x,c
	print(xm,cm)

