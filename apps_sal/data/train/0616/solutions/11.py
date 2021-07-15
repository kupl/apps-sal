def countt(n):
 for i in range(5):
  pass
 return n
t = int(input())
for _ in range(t):
 m, n = map(int, input().split())
 arr = []
 p = []
 for x in range(m):
  temp = [i for i in input().split()]
  if(x % 2 == 0):
   for j in range(n):
    if(temp[j] == 'P'):
     p.append([x+1,j+1])
  else:
   for j in range(n-1, -1, -1):
    if(temp[j] == 'P'):
     p.append([x+1, j+1])
  arr.append(temp)
 c = countt(20)
 res = c
 l = len(p)
 for i in range(l):
  if(i+1 < l):
   res += abs(p[i][0] - p[i+1][0]) + abs(p[i][1] - p[i+1][1])
 print(res-c)
