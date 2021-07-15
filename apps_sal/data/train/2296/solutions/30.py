
import sys
from collections import deque, defaultdict
import copy
import bisect
sys.setrecursionlimit(10 ** 9)
import math
import heapq
from itertools import product, permutations,combinations
import fractions

import sys
def input():
	return sys.stdin.readline().strip()

S = input()

alpha = defaultdict(int)
N = len(S)
for i in range(N):
	alpha[S[i]] += 1

num = 0
for n in alpha:
	if alpha[n] % 2 == 1:
		num += 1

if num >= 2:
	print((-1))
	return

alpha_num = defaultdict(deque)
for i in range(N):
	alpha_num[S[i]].append(i)

loc_list = [-1]*N
num = 0
for i in range(N):
	if len(alpha_num[S[i]]) >= 2:
		x = alpha_num[S[i]].popleft()
		y = alpha_num[S[i]].pop()
		loc_list[x] = num
		loc_list[y] = N - 1 - num
		num += 1
	elif len(alpha_num[S[i]]) == 1:
		x = alpha_num[S[i]].popleft()
		loc_list[x] = N // 2

class Bit:
	def __init__(self, n):
		self.size = n
		self.tree = [0] * (n + 1)

	def sum(self, i):
		s = 0
		while i > 0:
			s += self.tree[i]
			i -= i & -i
		return s

	def add(self, i, x):
		while i <= self.size:
			self.tree[i] += x
			i += i & -i


bit = Bit(N)
ans = 0



for i, p in enumerate(loc_list):
	bit.add(p + 1, 1)
	ans += i + 1 - bit.sum(p + 1)

print(ans)

