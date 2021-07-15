t = int(input())
for i in range(t):
 i,j= list(map(int,input().split()))
 base1=i
 base2=j
 arr1=[]
 arr2=[]
 while base1>0 :
  arr1.append(base1)
  base1=base1/2
 while base2>0 :
  arr2.append(base2)
  base2=base2/2
 n1=len(arr1)
 n2=len(arr2)
 n=min(n1,n2)
 dist=-1
 for i in range(n):
  if arr1[n1-1-i]!=arr2[n2-1-i]:
   dist=n1+n2-2*i
   break
 if dist==-1:
  dist=max(n1,n2) -n
 print(dist)



