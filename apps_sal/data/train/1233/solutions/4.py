import sys
import math
from collections import defaultdict,Counter

# input=sys.stdin.readline
# def print(x):
#     sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP1/output.txt",'w')
# sys.stdin=open("CP1/input.txt",'r')

def possible(n1,n):
	# d=defaultdict(int)
	odd=set()
	# even=set()
	for j in range(n):
		# print(odd)
		if s[j] in odd:
			odd.remove(s[j])
			# even.add(s[j])
		else:
			odd.add(s[j])
		# d[s[j]]+=1
		# print(odd)
		if j<n1-1:
			continue
		# print(j)
		if len(odd)==1:
			return True

		if s[j-n1+1] in odd:
			odd.remove(s[j-n1+1])
			# even.add(s[j])
		else:
			odd.add(s[j-n1+1])
	return False
# m=pow(10,9)+7
t=int(input())
for i in range(t):
	s=list(input())
	n=len(s)
	ans=1
	for j in range(n,1,-1):
		if possible(j,n):
			ans=j
			break
	print(ans)
	# low=1
	# high=n
	# while low<=high:
	# 	mid=(low+high)//2
	# 	if mid%2==0:
	# 		if low%2==0:
	# 			low+=1
	# 			mid+=1
	# 		elif high%2==0:
	# 			high-=1
	# 			mid-=1
	# 	# if low>high:
	# 	# 	break
	# 	if possible(mid,n):
	# 		low=mid+1
	# 	else:
	# 		high=mid-1
	# 	print(mid,low,high)
	# print(mid)

