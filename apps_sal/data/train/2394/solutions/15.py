t = int(input())
for _ in range(t):
	n = int(input())
	s = list(input())
	p = [0]
	for x in s:
		if x == '(':
			p.append(p[-1] + 1)
		else:
			p.append(p[-1] - 1)
	print(-min(p))

