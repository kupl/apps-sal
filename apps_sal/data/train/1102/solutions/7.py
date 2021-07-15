# cook your dish here


arr=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
t=int(input())
for i in range(0,t):
 n=str(input())
 l=len(n)
 n=int(n)
 
 p=n
 hi=1
 while p>1:
  j=p%10
  j=int(j)
  if j>1:
   
   hi=hi*len(arr[j-2])
   
  p=p/10
 
 
 print(hi)
 

