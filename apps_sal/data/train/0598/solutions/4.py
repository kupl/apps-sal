import sys
def stone(s):
 n,k = list(map(int,s.split()))
 l = list(map(int,sys.stdin.readline().split()))
 if k%2 == 1:
  k = 1
 
 elif k%2 == 0 and k != 0:
  k = 2
 else:
  k = 0
 for j in range(k):
  m = max(l)
  for i in range(n):
   l[i] = m - l[i]
 s1 = ''
 for i in range(n):
  s1 += (str(l[i]) + ' ')
 print(s1)
stone(sys.stdin.readline()) 
