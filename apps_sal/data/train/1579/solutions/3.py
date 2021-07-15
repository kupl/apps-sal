T = int(input())
ans = []

for _ in range(T):
 N = int(input())
 A = [int(i) for i in input().split()]

 if(N>62):
  ans.append('NO')
 else:
  D = {}
  flag = True
  for i in range(N):
   x = 0
   for j in range(i,N):
    x |= A[j]
    if(x in D):
     flag = False
     break
    D[x] = True
   if(not flag):
    break
  if(flag):
   ans.append('YES')
  else:
   ans.append('NO')

for i in ans:
 print(i)

