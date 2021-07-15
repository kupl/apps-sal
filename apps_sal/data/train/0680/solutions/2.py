# cook your dish here
import sys
input = sys.stdin.readline
mxn=998244353
for _ in range(int(input())):
 n,m=list(map(int,input().split()))
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 s1=sum(a)%mxn
 s2=sum(b)%mxn
 for q in range(int(input())):
  ls=input().split()
  if int(ls[0])==3:print((s1*s2)%mxn)
  else:
   t,l,r,x=list(map(int,ls))
   if t==1:
    s1=(s1+(r-l+1)*x)%mxn
   else:
    s2=(s2+(r-l+1)*x)%mxn


