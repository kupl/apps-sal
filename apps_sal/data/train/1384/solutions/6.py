for _ in range(int(input())):
 (n,k)=(int(x) for x in input().split())
 a = input()
 hidari=[0]*n
 migi=[0]*n
 for i in range(n-k+1):
  loli=i
  i-=1
  num=0
  while i>=0:
   if a[i]=="1":
    num+=1
    i-=1
   else:
    break
  hidari[loli]=num
 for j in range(k-1,n):
  kaori=j
  j+=1
  num=0
  while j<=n-1:
   if a[j]=="1":
    num+=1
    j+=1
   else:
    break
  migi[kaori]=num
 if (n==k):
  print(n)
 else:
  max=0
  for i in range(n-k+1):
   if max<hidari[i]+k+migi[i+k-1]:
    max=hidari[i]+k+migi[i+k-1]
  print(max)

