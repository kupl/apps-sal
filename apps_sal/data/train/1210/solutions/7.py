for tt in range(int(input())):
 n,p = list(map(int,input().strip().split()))
 d,l = list(map(str,input().strip().split()))
 
 if d=='L':
  if p&1:
   print(p,l)
  else:
   if l=='E':
    tl = 'H'
   else:
    tl = 'E' 
   print(p,tl)
 else:
  np = n - p + 1
  if n&1:
   if p&1:
    tl = l
   else:
    if l =='E':
     tl = 'H'
    else:
     tl = 'E'
  else:
   if p&1:
    if l=='E':
     tl = 'H'
    else:
     tl ='E'
   else:
    tl = l
  print(np,tl)

