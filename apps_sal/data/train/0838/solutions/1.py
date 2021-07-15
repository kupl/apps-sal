# cook your dish here
t=int(input())
while t:
 t=t-1
 n = int(input())
 l = list(map(int,input().split()))
 l.reverse()
 c = 0
 for i in range(n):
  if(c>=l[i]):
   pass
  else:
   c = l[i]
  c = c+1
 print(c-1)
