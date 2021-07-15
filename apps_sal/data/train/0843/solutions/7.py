for _ in range(int(input())):
 n = int(input())
 s = 0
 mat = []
 
 for i in range(n):     
  a = []
  a = [int(i) for i in input().split()] 
  a.sort()
  mat.append(a)
 
 ans = mat[n-1][n-1]; last = mat[n-1][n-1]
 
 s = 1
 
 for i in range(n-2,-1,-1):
  for j in range(n-1,-1,-1):
   if mat[i][j]<last:
    ans += mat[i][j]
    last = mat[i][j]
    s+=1
    break
 
 if s==n:print(ans)
 else:print(-1)
