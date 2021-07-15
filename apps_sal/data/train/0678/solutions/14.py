t = int(input())
for i in range(0,t):
 n = int(input())
 arr = list(map(int, input().split(' ')))
 for j in range(1,n):
  arr[j]+=arr[j-1]
 j=0
 days = 0
 while True:
  days+=1
  j+=arr[j]
  if(j >= n-1):
   break
 print(days)

