for _ in range(int(input())):
 a,b=input().split()
 a=int(a)
 onec=0
 zeroc=0
 for i in range(a):
  stk=input()
  if stk[0]=='0':
   zeroc+=stk.count('0')
  else:
   onec+=stk.count('1')
 if b=='Dee':
  if zeroc>onec:
   print('Dee')
  else:
   print('Dum')
 else:
  if onec>zeroc:
   print('Dum')
  else:
   print('Dee')
