from sys import stdin
input=stdin.readline
for i in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 if all((a[i] < a[i + 1] for i in range(n - 1))):
   print(n * (n + 1) // 2 - 1)
   continue
 for i in range(1, n):
  if a[i - 1] >= a[i]:
   arr1 = a[:i]
   break
 for j in range(n - 1, 0, -1):
  if a[j - 1] >= a[j]:
   arr2 = a[j:]
   break

 ans=len(arr1)+len(arr2)
 le=len(arr2)
 x=0
 for i in arr1: 
  while x<len(arr2) and arr2[x]<=i:
   x+=1
   le-=1
  if x==len(arr2):
   break
  ans+=le
 print(ans)
