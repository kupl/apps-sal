import math
import itertools
import heapq
from sys import stdin, stdout, setrecursionlimit
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
 
 
# d = defaultdict(lambda: 0)
# setrecursionlimit(10**7)
# inf = float("inf")
 
 
##### stdin ####
def LM(t, r): return list(map(t, r))
def R(): return stdin.readline()
def RS(): return R().split()
def I(): return int(R())
def F(): return float(R())
def LI(): return LM(int,RS())
def LF(): return LM(float,RS())
def ONE_SL(): return list(input())
def ONE_IL(): return LM(int, ONE_SL())
def ALL_I(): return map(int, stdin)
def ALL_IL(): return LM(int,stdin)
 
##### tools #####
def ap(f): return f.append
def pll(li): print('\n'.join(LM(str,li)))
def pljoin(li, s): print(s.join(li))
 
 
 
##### main #####
 
class BIT(object):
 
	def __init__(self,l):
		self.size = l
		self.bit = [0]* (self.size+1)
 
	def sum(self, i):
		s = 0
		while i > 0:
			s += self.bit[i]
			i -= i & -i
		return s
 
	def add(self, i, x):
		while i < self.size:
			self.bit[i] += x
			i += i & -i
 
	def __str__(self):
		return str(self.bit)
 
 
def main():
	N,M = LI()
 
	bit = BIT(M+2)
	L = []
	R = []
	b = [[] for i in range(M+1)]
 
 
	for i in range(N):
		l,r = LI()
		L.append(l); R.append(r)
		b[r-l +1].append(i)
 
 
	gone = 0
	for d in range(1, M+1):
		for i in b[d]:
			gone+=1
			bit.add(L[i], 1)
			bit.add(R[i]+1, -1)
 
 
		ans = N-gone
 
		for m in range(d, M+1, d):
 
			ans += bit.sum(m)
		print(ans)
 
 
 
 
def __starting_point():
	main()
__starting_point()
