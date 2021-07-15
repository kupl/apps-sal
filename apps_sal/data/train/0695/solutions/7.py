for _ in range(int(input())):
 [x,y,n] = list(map(int , input().split()))
 
 if (x==y):
  print(0)
 else:
  sn = bin(n)[2:]
  ln = len(sn)

  sx = bin(x)[2:]
  lx = len(sx)

  sy = bin(y)[2:]
  ly = len(sy)

  l = max(ln,lx,ly)
  
  sn = '0'*(l-ln) + sn
  sx = '0'*(l-lx) + sx
  sy = '0'*(l-ly) + sy

  for i in range(l):
   if (sx[i] != sy[i]):
    break
  #print("i = ",i)

  if (i == 0):
   t1 = 1
  else:
   t1 = int(sn[:i],2)+1

  rstval = 2**(l-i-1)

  #no limits
  if (sx[i] == '0' and sn[i] == '1'):
   print(t1 * rstval)
  
  elif (sx[i] == '1' and sn[i] == '1'):
   #print(256)
   if (i == l-1):
    t2 = 1
   else:
    t2 = int(sn[i+1:],2)+1
   print(t2 + (t1-1)*rstval)

  elif (sx[i] == '1' and sn[i] == '0'):
   t2 = rstval
   print((t1-1)*t2)

  #limits
  else:
   if (i == l-1):
    t2 = 1
   else:
    t2 = int(sn[i+1:],2)+1
   print(t2 + (t1-1)*rstval)
