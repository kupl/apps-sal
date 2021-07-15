for test_ in range(int(input())):
 n = int(input())
 op = [[0 for i in range(n)] for i in range(n)]
 #num = list(range(1,n*n+1))
 i = 0
 j = 0
 num = 1
 while i<n and j<n:
  temp1 = i
  temp2 = j
  while temp1<=j:
   op[temp1][temp2] = num
   num += 1
   temp1 += 1
   temp2 -= 1
  if j!=n-1:
   i = 0
   j += 1
  else:
   i += 1
   j = n-1
 for i in op:
  print(*i)
