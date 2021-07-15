
T = int(input())
for t in range(T):
	N = int(input())
	p = []
	q = []
	for n in range(N):
		x = input().split()
		if x[0] == 'Right':
			p.append('Left')
		elif x[0] == 'Left':
			p.append('Right')
		q.append(' '.join(x[2:]))
	p.append('Begin')
	for n in range(N):
		print(p[-1-n], 'on', q[-1-n])
	print()
