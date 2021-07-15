for _ in range(int(input())):
 n = int(input())
 s = 0
 m = []
 
 for i in range(n):     
  l = []
  l = [int(i) for i in input().split()] 
  l.sort()
  m.append(l)
 
 answer = m[n-1][n-1]; last = m[n-1][n-1]
 
 s = 1
 
 for i in range(n-2,-1,-1):
  for j in range(n-1,-1,-1):
   if m[i][j]<last:
    answer += m[i][j]
    last = m[i][j]
    s+=1
    break
 
 if s==n:print(answer)
 else:print(-1)
