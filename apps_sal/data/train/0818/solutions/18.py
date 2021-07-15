for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 MAT=[0]
 cur=0
 for i in range(n):
  if a[i]%2==0:
   cur+=1
  MAT.append(cur)
 for i in range(int(input())):
  l,r=map(int,input().split())
  if MAT[r]-MAT[l-1]==0:
    print("ODD")
  else:
   print("EVEN")
