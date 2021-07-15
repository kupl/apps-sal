# cook your dish here

def count(res):
 sum=0
 for items in result:
  sum=sum+1
 return sum 
 
import itertools
arr=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
t=int(input())
for i in range(0,t):
 n=str(input())
 l=len(n)
 n=int(n)
 s=""
 p=n
 hi=1
 while p>0:
  j=p%10
  j=int(j)
  if j>1:
   #s=s+arr[j-2]
   #result=itertools.combinations(arr[j-2],1)
   hi=hi*len(arr[j-2])
   
  p=p/10
 #result=itertools.combinations(s,l)
 
 print(hi)
 

