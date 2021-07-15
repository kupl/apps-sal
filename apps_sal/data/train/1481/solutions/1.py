a = int(input())
for i in range(a):
 b = list(map(int,str(input())))
 if len(b)%2!=0:
  print(-1)
 else:
  if sum(b)==len(b) or sum(b)==0:
   print(-1)
  else:
   print(abs((len(b)//2)-sum(b)))
