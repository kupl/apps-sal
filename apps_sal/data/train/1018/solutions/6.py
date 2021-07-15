t = int(input())

for _ in range(t):
 n = int(input())
 A = list(map(int,input().split()))
 min = A[0] - A[1]
 for i in range(1,n-1):
  t = A[i] - A[i+1]
  if(t<min):
   min = t
 print(min)
