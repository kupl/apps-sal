from bisect import bisect_left, bisect_right, insort_left
import sys
readlines = sys.stdin.readline
def main():

	n = int(input())
	s = list(input())
	q = int(input())

	d = {}
	flag = {}
	for i in list('abcdefghijklmnopqrstuvwxyz'):
		d.setdefault(i, []).append(-1)
		flag.setdefault(i, []).append(-1)
	for i in range(n):
		d.setdefault(s[i], []).append(i)
	for i in range(q):
		q1,q2,q3 = map(str,input().split())
		if q1 == '1':
			q2 = int(q2) - 1
			if s[q2] != q3:
				insort_left(flag[s[q2]],q2)
				insort_left(d[q3],q2)
				s[q2] = q3
		else:
			ans = 0
			q2 = int(q2) - 1
			q3 = int(q3) - 1
			if q2 == q3:
				print(1)
				continue
			for string,l in d.items():
				res = 0
				if d[string] != [-1]:
					left = bisect_left(l,q2)
					right = bisect_right(l,q3)
				else:
					left = 0
					right = 0
				if string in flag:
					left2 = bisect_left(flag[string],q2)
					right2 = bisect_right(flag[string],q3)
				else:
					left2 = 0
					right2 = 0
				if left != right:
					if right - left > right2 - left2:
						res = 1
				ans += res
				#print(string,l,res)
			print(ans)
def __starting_point():
	main()
__starting_point()
