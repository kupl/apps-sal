from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import math

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

class SegTree:
	def __init__(self, size):
		self.n = size
		self.T = [[INF, INF] for _ in range(4*self.n)]

	def _update_range(self, v, tl, tr, l, r, val):
		if l > r or tl > tr: return
		# print(f"l, r = {l, r}, tl, tr = {tl, tr}")
		if l == tl and r == tr:
			# self.T[v].append(val)
			if self.T[v] == [INF, INF]:
				self.T[v] = val
		else:
			mid = (tl + tr)//2
			self._update_range(2*v, tl, mid, l, min(r, mid), val)
			self._update_range(2*v+1, mid+1, tr, max(l, mid+1), r, val)

	def update_range(self, l, r, val):
		self._update_range(1, 0, self.n-1, l, r, val)


	def qry(self, index):
		return self._qry(1, 0, self.n-1, index)

	def _qry(self, v, tl, tr, index):
		if tl == tr:
			if self.T[v]:
				return self.T[v]
			else:
				return (INF, INF)
		else:
			mid = (tl + tr)//2
			curr_x, curr_time = INF, INF
			if self.T[v]:
			 	curr_x, curr_time = self.T[v]
			if index <= mid:
				prev_x, prev_time = self._qry(2*v, tl, mid, index)
			else:
				prev_x, prev_time = self._qry(2*v+1, mid+1, tr, index)
			if curr_time < prev_time:
				return (curr_x, curr_time)
			else:
				return (prev_x, prev_time)

def main():
	# n = number of knights
	# m = number of fights
	n, m = rli()
	ans = [0 for _ in range(n)]
	ST = SegTree(n)
	for time in range(m):
		l, r, x = rli()
		l -= 1
		r -= 1
		x -= 1
		ST.update_range(l, x-1, (x, time))
		ST.update_range(x+1, r, (x, time))

	for i in range(n):
		k, _ = ST.qry(i)
		ans[i] = k + 1 if k < INF else 0
	print(" ".join(str(x) for x in ans))
	stdout.close()

def __starting_point():
	main()
__starting_point()
