n = int(input())
h = input()
d = []
for _ in range(n):
	s = input()
	fr = s[:3]
	to = s[5:]
	if (to, fr) in d:
		del d[d.index((to, fr))]
	else:
		d.append((fr, to))
if len(d):
	print('contest')
else:
	print('home')
