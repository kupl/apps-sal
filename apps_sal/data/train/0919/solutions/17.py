# cook your dish here
import sys
T=int(input())
for i in range(T):
 n=int(input())
 seq=list(map(int,input().split(" ")))
 t=[-sys.maxsize-1 for i in range(n)]
 t[0]=0
 for i in seq:
  x=i
  even=t[0]
  odd=t[x]
  
  t[x]=max(odd,even+1)
  t[0]=max(even,odd+1)
  
 print(n-t[0])
   
 

