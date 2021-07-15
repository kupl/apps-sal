# cook your dish here
t=int(input())

for i in range(t):
 n,k=map(int,input().split())
 l=[]
 l1=list(map(str,input().split()))
 for i in range(k):
  l2=list(map(str,input().split()))
  l=l+l2
 for a in l1:
  if a in l:
   print("YES",end=" ")
  else:
   print("NO",end=" ")
 
 print()
