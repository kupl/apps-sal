import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int,minp().split()))

def solve():
	n = mint()

	s = list(minp())
	t = list(minp())
	if sorted(t) != sorted(s):
		print("NO")
		return

	for i in range(26):
		if s.count(chr(ord('a')+i)) > 1:
			print("YES")
			return
	r = 0
	for i in range(len(s)):
		for j in range(i+1,len(s)):
			if t.index(s[i]) > t.index(s[j]):
				r += 1
	#print(r)
	print(["NO","YES"][r%2 == 0])

for i in range(mint()):
	solve()

