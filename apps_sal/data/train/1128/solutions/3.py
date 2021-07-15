import sys

t = eval(input())
for i in range(t):
 n = eval(input())
 a = list(map(int, input().split()))
 ch = 0
 for i in range(n):
  if(sum(a[:i]) == sum(a[i + 1:])):
   print(i)
   ch = 1
   break
 if(ch == 0):
  print(-1)
    

