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

	def SegAdd(self, l, r, x):#lからrにxを足す
		self.PointAdd(l, x)
		self.PointAdd(r+1, -x)
		return

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: x[1]-x[0])
b = BIT(m)

too_long = n #r-l+1よりも大きい区間（必ず訪れる）
cur = 0
for i in range(1, m+1):
	while cur < n and s[cur][1]-s[cur][0]+1 < i:
		too_long -= 1
		b.SegAdd(s[cur][0], s[cur][1], 1)
		cur += 1
	ans = too_long
	for j in range(i, m+1, i):
		ans += b.Sum(j)
	print(ans)
