# cook your dish here
n=int(input())
s=set()
for i in range(n):
	x,d =map(int,input().split())
	if (x+d,-d) in s:
		print('YES')
		return
	s.add((x, d))
print('NO')
