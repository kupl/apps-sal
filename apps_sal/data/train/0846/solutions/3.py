import sys
import math
from collections import defaultdict,Counter

# input=sys.stdin.readline
# def print(x):
#     sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP3/output.txt",'w')
# sys.stdin=open("CP3/input.txt",'r')

# mod=pow(10,9)+7
k,a,b=list(map(int,input().split()))
if b<=a+2 or k<=a:
	ans=1+k
else:
	k-=a-1
	ans=a+k//2*(b-a)
	if k&1:
		ans+=1
print(ans)

