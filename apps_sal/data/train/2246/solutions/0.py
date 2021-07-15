from sys import stdin
from heapq import heappop,heappush
def main():
	n,k = map(int,stdin.readline().split())
	X = list(map(int,stdin.readline().split()))
	A = int(stdin.readline().strip())
	C = list(map(int,stdin.readline().split()))
	l  = list()
	i = 0;g = k;ans = 0;flag = True
	while i < n and flag:
		heappush(l,C[i])
		if X[i] > g:
			while len(l)!= 0 and X[i] > g:
				ans+= heappop(l)
				g+= A
			if len(l) == 0 and X[i] > g:
				flag = False
		i+=1
	if flag:
		print(ans)
	else:
		print(-1)
main()
