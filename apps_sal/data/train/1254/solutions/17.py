t = int(input())
for i in range(t):
  n,p = list(map(int, input().split(' ')))
  
  z= list(map(int, input().split()))
  e = 0
  d = 0
  for j in z:
   if j >= int(p/2):
    e = e+1 
   elif j <= int(p/10):
    d = d+1
  if e == 1 and d == 2:
   print('yes')
  else:
   print('no')

