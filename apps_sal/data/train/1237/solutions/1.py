# cook your dish here
test=int(input())
for _ in range(test):
  a,b,c=[int(x) for x in input().split()]
  t=s=0
  m=100*a+b
  while a*100+b>c and t<=10000:
    if b<c:
      a-=1
      b+=100
    b-=c
    temp=b
    b=a
    a=temp
    t+=1
    if a*100+b>m:
      m=a*100+b
      s=t
  print(s)
