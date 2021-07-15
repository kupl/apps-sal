import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1:
		print (0)
		continue
	dec = 0
	ind = -1
	for i in range(n-2,-1,-1):
		if a[i]<a[i+1]:
			dec = 1
		elif a[i]>a[i+1] and dec:
			ind = i
			break
	print (ind+1)
