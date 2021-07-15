t=int(input())
for i in range(t):
 n,m=[int(x) for x in input().split()]
 amt=[int(x) for x in input().split()]
 cost=0
 brr=[0 for x in range(n)]
 crr=[]
 for j in range(n):
  d,f,b=[int(x) for x in input().split()]
  if(amt[d-1]>0):
   amt[d-1]-=1
   cost+=f
   brr[j]=d
  else:
   crr.append(j)
   cost+=b
 r=0
 for j in crr:
  for k in range(r,m):
   if(amt[k]>0):
    r=k
    amt[k]-=1
    brr[j]=k+1
    break
 print(cost)
 for j in range(n-1):
  print(brr[j],end=" ")
 print(brr[-1])

