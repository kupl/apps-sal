def e(s):return f([*s,'+'])
def f(s,r=0,o=0,x='',c=0):
 while s and')'!=c:
  c=s.pop(0);i='+-*/)('.find(c)
  if c=='-'>x or i<0:x+=c
  elif c=='(':x=str(f(s))
  elif i>-1:a=float(x);r=[r+a,r-a,r*a,r/a][o];o=i;x=''
 return r
