n, m = [int(x) for x in input().split()]
l = [[]] * n
for i in range(n):
	l[i] = set(int(x) for x in input().split()[1:])
while True:
	for i in range(len(l)):
		for j in range(i):
			if l[i] & l[j]:
				l[j] |= l[i]
				l = l[:i] + l[i + 1:]
				break
		else:
			continue
		break
	else:
		break
ans = len(l)
for s in l:
	if s:
		ans -= 1
		break
print(ans)

