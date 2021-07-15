t=eval(input())
while t>0:
  t=t-1
  f1,f2,r1,r2,r3,r4=list(map(int,input().split()))
  p1,p2,p3,p4=list(map(float,input().split()))
  s1=(1-p1)*(-f1)+(r2-f1)*(1-p2)*p1+p1*p2*(r1-f1)
  s2=(1-p3)*(-f2)+(r3-f2)*(p3)*(1-p4)+p3*p4*(r3+r4-f2)
  if s1>s2:
    print('FIRST')
  elif s1<s2:
    print('SECOND')
  else:
    print('BOTH')
    

