for _ in range(int(input())):
 m,c,h=(list(map(int,input().split())))
 if c+ 2*m < h- m:
  print('Yes')
 elif h==c:
  print('No')
 else:
  diff = h - c
  if (h-c)%3==0:
   if (h-c)//3<=m:
    print('No')
   else:
    print('Yes')
  else:
   print('Yes')
   

