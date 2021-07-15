t = int(input())
for i in range(t):
 dee = 0
 dum = 0
 [n, start] = input().split(' ')
 n=int(n)
 #print(n,starter)
 for k in range(n):
  pile = input()
  if pile[0] == '0':
   dee += pile.count('0')
  else:
   dum += pile.count('1')
 if start == 'Dum':
  if dum>dee:
   print('Dum')
  else:
   print('Dee')
 else:
  if dum<dee:
   print('Dee')
  else:
   print('Dum')
