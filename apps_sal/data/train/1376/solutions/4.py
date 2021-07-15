def abc(balls, n):
 y = n
 i = 0
 while(y):
  if i<=n and balls[i]==0:
   i = i+1
   continue
  c1 = i
  if balls[i]>=2:
   balls[i] -= 2
   m1 = 2
   c2 = n
   m2 = 0
  else:
   m1 = 1
   balls[i] = 0
   j = i
   while(j<n and balls[j]==0):
    j = j+1
   i = j
   c2 = i
   balls[i] -= 1
   m2 = 1
  print(c1,m1,c2,m2)
  y = y-1
   
 
for _ in range(int(input())):
 n, k = list(map(int, input().split()))
 balls = list(map(int, input().split()))
 
 if k==2:
  abc(balls, n)
  continue
 
 # y = n
 # missing = n
 # temp = []
 # for i in range(i+1):
 #     if balls[i]!=0:
 #         temp.append(i)
 #     else:
 #         missing = i
 #         n = n-1
   
 arr = []
 for i in range(n+1):
  arr.append([balls[i], i])
 arr = sorted(arr, key=lambda x:x[0])
 # print(arr)
 
 i = 0
 j = n
 y = n
 while(arr[j][0] == 0):
  j = j-1
 
 while(y):
  if i==j:
   print(arr[i][1], arr[i][0], n, 0)
   continue
  x = k
  c1 = arr[i][1]
  if x<=arr[i][0]:
   arr[i][0] = arr[i][0]-x;
   m1 = k
   m2 = 0
   c2 = n
  else:
   x = k - arr[i][0]
   m1 = arr[i][0]
   arr[i][0] = 0
   c2 = arr[j][1]
   m2 = min(arr[j][0], x)
   arr[j][0] = max(arr[j][0]-x, 0)
  
  if(arr[j][0] == 0):
   j = j-1
  if(arr[i][0] == 0):
   i = i+1
  print(c1,m1,c2,m2)
  y = y-1

