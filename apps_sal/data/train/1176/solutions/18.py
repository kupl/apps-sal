t = int(input())
while t>0:
 t -= 1
 s = input()
 if len(s)<4:
  print('NO')
  continue
 if(s[-4:]!='1000'):
  print('NO')
 else:
  print('YES')
