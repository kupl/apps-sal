# cook your dish here
T = int(input())
for i in range(T):
 N = int(input())
 P = input()
 P = P.split()
 p = []
 for j in P:
  p.append(int(j))
 count = 1
 for i in range(1,N):
  minval=p[i]
  if i<6 and minval<min(p[:i]):
   count += 1
  elif i>=6 and minval<min(p[i-5:i]):
   count += 1
 print(count)
