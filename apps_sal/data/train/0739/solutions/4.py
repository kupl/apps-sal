
def my_sqrt(v):
 v*=100
 lo=0
 hi=v
 while lo+1<hi:
  mi = (lo + hi) >> 1
  if mi*mi<=v:
   lo=mi
  else:
   hi=mi
 return lo

def solve():
 dir=0
 dx=[0,-1,0,1]
 dy=[1,0,-1,0]
 x,y=0,0
 line=input()
 ss=line.split()
 n=len(ss)
 i=0
 while(i<n):
  if(ss[i]=='L'):
   dir=(dir+1)%4
  elif ss[i]=='R':
   dir=(dir+3)%4
  else:
   x+=dx[dir]*int(ss[i])
   y+=dy[dir]*int(ss[i])
  i=i+1
 if x==0 and y==0:
  print('0.0')
  return
 v = my_sqrt(x*x+y*y)
 ds=''
 if(y>0):
  ds+='N'
 elif y<0:
  ds+='S'
 if(x>0):
  ds+='E'
 elif x<0:
  ds+='W'
 print('%d.%d%s' % (v/10, v%10,ds))

T=int(input())
while(T>0):
 T=T-1
 solve()
