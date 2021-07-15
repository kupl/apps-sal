for i in range(int(input())):
 h = int(input())
 f = []
 ans = []
 for j in range(0,h):
  f.append(list(map(int,input().split())))
 for k in range(0,h):
  sum1 = 0
  sum2 = 0
  for l in range(0,k+1):
   sum1 += f[l][h+l-k-1]
   sum2 += f[h+l-k-1][l]
   
  ans.append(sum1)
  
  ans.append(sum2)
  
 print(max(ans))

