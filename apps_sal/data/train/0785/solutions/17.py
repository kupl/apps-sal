try:
 t=int(input())
 for i in range(0,t):
  a=int(input())
  s=0
  f=0
  j=1
  flist=[]
  max=0
  k=0
  g=1
  # print('ff')
  while(g>0):
   # print('hjh')
   s=s+a
   f=f+(2**(j-1))
   j=j+1
   g=s-f
   if(g>max):
    max=g
    k=j
  print(f'{j-2} {k-1}')
except:
 pass
