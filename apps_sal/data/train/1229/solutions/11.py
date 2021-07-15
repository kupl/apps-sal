test=int(input())
for x in range(test):
 n,k = list(map(int, input().split()))
 a=list(map(int, input().split()))
 
 tonu=[]
 monu=[]
 
 for i in range(n):
  if ((i+1)%2==0):
   tonu.append(a[i])
  else:
   monu.append(a[i])
 
 tonu.sort()
 monu.sort(reverse= True)
 
 for i in range(k):
  if (sum(tonu)>sum(monu) or (i==len(tonu) or i==len(monu))):
   break
  tonu[i],monu[i]=monu[i],tonu[i]
 
 if sum(tonu)>sum(monu):
  print("YES")
 else:
  print("NO")

