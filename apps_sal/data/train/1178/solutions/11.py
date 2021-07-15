# cook your dish here
t=int(input())
for i in range(t):
 n=int(input())
 arr=list(map(int,input().split()))
 if 0 not in arr:
  print(0)
 elif arr.count(0)==len(arr):
  print(n)
 else:
  c=0
  arr.sort()
  for k in arr:
   if c>=k:
    c+=1
   else:
    break
  print(c)
