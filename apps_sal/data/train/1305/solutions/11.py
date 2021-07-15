t=int(input())
for _ in range(t):
 n=int(input())
 cnt=0
 arr = [[0 for j in range(n)] for i in range(n)]
 for i in range(n):
  l=list(map(int,input().split()))
  arr.insert(i,l)
  arr.pop()
 for i in range(n-1):
  for j in range(n-1):
   if arr[i][j]==arr[i][j+1]:
    if arr[i][j+1]==1:
     cnt=1
     break
   elif arr[i][j]==arr[i+1][j]:
    if arr[i+1][j]==1:
     cnt=1
     break
 if cnt==0:
  print("SAFE")
 else:
  print("UNSAFE")
