#list_int 並べて出力 print (' '.join(map(str,ans_li)))
#list_str 並べて出力 print (' '.join(list))

from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = int(input())
aa = list(map(int,list(input())))
bb = list(map(int,list(input())))
x00 = x01 = x10 = x11 = 0

for i in range(N):
	if aa[i] and bb[i]:
		x11 += 1
	elif not aa[i] and bb[i]:
		x01 += 1
	elif aa[i] and not bb[i]:
		x10 += 1
	else:
		x00 += 1

print(x00*(x10+x11)+x10*x01)

