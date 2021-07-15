n=int(input())
while(n>0):
 x,y,z=map(int,input().split())
 t=(x+y)//z
 if t%2==0:
  print('Chef')
 else:
  print('Paja')
 n-=1
