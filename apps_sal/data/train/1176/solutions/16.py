t=int(input())
for _ in range(t):
 s=input()
 if len(s)>=4:
  x=s[-4]+s[-3]+s[-2]+s[-1]
  if x=='1000':
   print('YES')
  else:
   print('NO')
 else:
  print('NO')

