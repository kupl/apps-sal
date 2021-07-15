# cook your dish here
t = int(input())
for _ in range(t) :
 n = int(input())
 arr = list(map(int,input().split()))
 arr.sort()
 c = 0
 for i in range(n) :
  if arr[i] <= c :
   c += 1
  else :
   break
 print(c)
