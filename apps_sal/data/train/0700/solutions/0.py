for t in range(int(input())):
 n = int(input())
 l = []
 m = []
 x = list(map(int,input().split()))
 l.append(x)
 m.append(list(x))
 for i in range(1,n):
  x = list(map(int,input().split()))
  l.append(x)
  temp = []
  for i in range(4):
   temp.append (x[i]+min(m[-1][:i]+m[-1][i+1:]))
  m.append(temp)
 print(min(m[-1]))
