for test in range(int(input())):
 no=int(input())
 a=input()
 b=input()
 if a.count('0')==b.count('0') and a.count('1')==b.count('1'):
  c=0
  for i in range(len(b)):
   if b[:i].count('1')>a[:i].count('1'):
    c=1
    break
  if c==0:
   print('Yes')
  else:
   print('No')
 else:
  print('No')
