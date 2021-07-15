import bisect
class b:
	def __init__(self, loc, val, ls):
		self.loc = loc
		self.val = val
		self.ls = ls
		self.done = False
		self.ans = -1

	def do(self):
		if self.done: return self.ans
		x = bisect.bisect_left(self.ls, self.loc-self.val) - 1
		if x == -1: self.ans = 0
		else:
			self.ans = ls[x].do() + 1
		self.done =True
		return self.ans

	def __lt__(self, obj):
		if type(obj) == int: return obj > self.loc
		return obj.loc > self.loc

ls = []
for _ in range(int(input())):
	x,y = map(int, input().split(" "))
	ls.append(b(x, y, ls))
ls.sort()
m = -1
for l in ls:
	m = max(m, l.do())
print(len(ls) - (m+1))
