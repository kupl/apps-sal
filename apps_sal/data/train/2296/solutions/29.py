import sys
def input():
	return sys.stdin.readline()[:-1]

class BIT():#1-indexed
	def __init__(self, size):
		self.table = [0 for _ in range(size+2)]
		self.size = size

	def Sum(self, i):#1からiまでの和
		s = 0
		while i > 0:
			s += self.table[i]
			i -= (i & -i)
		return s

	def PointAdd(self, i, x):#
		while i <= self.size:
			self.table[i] += x
			i += (i & -i)
		return

s = input()
n = len(s)
a = [-1 for _ in range(n)]
ch = [[] for _ in range(26)]
for i in range(n):
	ch[ord(s[i])-97].append(i)
if sum([len(x)%2 == 1 for x in ch]) > 1:
	print(-1)
	return

for i, c in enumerate(ch):
	tmp = i
	l = len(c)
	for j in range(l//2):
		a[c[j]] = tmp
		a[c[l-j-1]] = tmp
		tmp += 26
#print(a)

former, latter = 0, 0
half = False
d = dict()
cur = 0
bubble = []

ans = 0

for x in a:
	if x >= 0:
		if x not in d:
			d[x] = cur
			cur += 1
			former += 1
			ans += latter + half
		else:
			bubble.append(d[x])
			latter += 1
			if n%2 == 1 and not half:
				ans += 1
	else:
		half = True

bit = BIT(n//2+2)
for b in bubble:
	ans += bit.Sum(b+1)
	bit.PointAdd(b+1, 1)

print(ans)
