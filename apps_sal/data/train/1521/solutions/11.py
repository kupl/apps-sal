# less goooooooo
try:
    t = int(input())
except:
    return
for q in range(t):
	n = int(input())
	score = [0] * n
	l = []
	u = []
	for q in range(n):
		x,y = map(int, input().split())
		l.append([x,q])
		u.append([y,q])

	l.sort(key = lambda x:x[0], reverse = True)
	u.sort(key = lambda x:x[0])
	for i in range(n):
		score[u[i][1]] += i
		score[l[i][1]] += i

	print(*score)
