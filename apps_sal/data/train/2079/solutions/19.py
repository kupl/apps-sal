# from debug import debug
import sys; input = sys.stdin.readline
from math import log2
from collections import defaultdict
d = defaultdict(int)
for i in range(int(input().strip())):
	l = list(map(int, input().strip().split()))
	if l[0] == 1:
		u, v, w = l[1:]
		while u != v:
			if int(log2(u)) < int(log2(v)): u, v = v, u
			d[(u, u//2)] += w
			u = u//2
	else:
		u, v = l[1:]
		ans = 0
		while u != v:
			if int(log2(u)) < int(log2(v)): u, v = v, u
			ans += d[(u, u//2)]
			u = u//2
		print(ans)


