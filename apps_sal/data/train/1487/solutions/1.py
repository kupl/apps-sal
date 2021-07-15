for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 x = int(input())
 abox = 0
 bbox = 0
 i = 0
 j = n-1
 while n>0:
  if j!=i:
   v = x*arr[j]
   n-=1
   summ = 0
   for f in range(i,j):
    if summ+arr[f]<=v:
     summ+=arr[f]
     abox+=1
     n-=1
    else:
     arr[f] = summ+arr[f] - v
     i = f
     break
   bbox+=1
   j-=1
  elif j==i:
   if abox>=bbox:
    abox+=1
    n-=1
   else:
    bbox+=1
    n-=1

 print(abox,bbox)
