import sys
input = sys.stdin.readline
from collections import defaultdict
mod = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def main():
	N = int(input())
	jud = 0
	ans = 0
	S = 0
	m = INF
	for i in range(N):
		A, B = getlist()
		S += A
		if A != B:
			jud = 1
		if A > B:
			m = min(m, B)

	if jud == 0:
		print(0)
	else:
		print(S - m)


def __starting_point():
	main()
__starting_point()
