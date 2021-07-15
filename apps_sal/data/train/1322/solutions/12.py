# cook your dish here
import math
def solve():
 #n=int(input())
 
 #n,m,k,l,r=map(int,input().split())
 #l=list(map(int,input().split()))
 #l1=list(map(int,input().split()))
 n,k = list(map(int,input().split()))
 s = sorted(map(int,input().split()),reverse=True)
 while k<n and s[k-1] == s[k] :
  k += 1
 print(k)

t=int(input())
#t=1
#res=[]
for i in range(t):
 solve()

