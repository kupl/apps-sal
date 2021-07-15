import sys
import math
from collections import defaultdict,Counter
import bisect
input=sys.stdin.readline
def print(x):
    sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP1/output.txt",'w')
# sys.stdin=open("CP1/input.txt",'r')

def Sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
	    if (prime[p] == True):
		    for i in range(p * p, n + 1, p):
			    prime[i] = False
	    p += 1
    prime[0]= False
    prime[1]= False

    p1=[]
    for p in range(n + 1):
	    if prime[p]:
		    p1.append(pow(p,4))
    return p1

p=Sieve(10**5)
# mod=pow(10,9)+7
t=int(input())
for i in range(t):
	n=int(input())
	ans=bisect.bisect_right(p,n)
	print(ans)
