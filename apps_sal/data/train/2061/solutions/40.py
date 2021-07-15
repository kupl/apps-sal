def func(ary):
  a=ary[0:2]
  b=ary[2:4]
  c=ary[4:6]
  x=a[0]+b[0]+c[0]
  y=a[1]+b[1]+c[1]
  if x>0:
    x-=x//3
  else:
    x+=1+abs(x)//3
  if y>0:
    y-=y//3
  else:
    y+=1+abs(y)//3
  if x!=y:
    t=max(abs(x-1),abs(y-1))
    return t
  else:
    if x>0:
      x-=1
      if x==0:return 0
      if x==1:return 1
      return x+1
    else:return abs(x-1)+1
          


t=int(input())
query=[list(map(int,input().split())) for _ in range(t)]
for x in query:print((func(x)))

