t=int(input())
for i in range(t):
 a,o,g=map(int,input().split())
 diff=abs(a-o)
 if diff<=g:
  print(0)
 else:
  print(diff-g)
