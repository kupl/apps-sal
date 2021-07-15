tt = int(input())
for _ in range(tt):
 n,x = map(int, input().rstrip().split(' '))
 s, l = input().rstrip().split(' ')
 initial = l
 que = []
 for i in range(n):
  que.append(initial)
  if initial=='H':
   initial = 'E'
   continue
  elif initial=='E':
   initial = 'H'
   continue
 if s=='R':
  dd = n-x+1
  que = que[::-1]
  pp = que[-dd]
 else:
  dd = x
  pp = que[x-1]
 print(dd, end=" ")
 print(pp)
