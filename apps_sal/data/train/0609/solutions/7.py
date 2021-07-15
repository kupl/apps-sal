for i in range(int(input())):
 n,k=list(map(int,input().split()))
 q=[int(z) for z in input().split()]
 carry,flag=0,0
 for i in range(n):
  if q[i]+carry>=k:
   carry+=q[i]-k
  else:
   flag=1
   print(i+1)
   break
 if carry>0 and flag!=1:
  print(carry//k +1+n)
 elif carry==0 and flag!=1:
  print(n+1)
   

