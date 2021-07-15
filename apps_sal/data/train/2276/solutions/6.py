q = int(input())
for rquer in range(q):
	c, r = list(map(int, input().split()))
	matt = [list(map(int,input().split())) for i in range(c)]
	mat = [[matt[i][j] for i in range(c)] for j in range(r)]
	for i in range(r):
		mat[i].append(max(mat[i]))
		mat[i].reverse()
	mat.sort()
	mat.reverse()
	work = mat[:min(4, r)]
	for t in work:
		t.pop(0)
	r = min(4, r)
	wyn = 0
	for num in range(c**r):
		shif = [(num//(c**i))%c for i in range(r)]
		new = 0
		for i in range(c):
			kol = [work[j][(i + shif[j])%c] for j in range(r)]
			new += max(kol)
		wyn = max(wyn, new)
	print(wyn)

