import math
d=10**8
e=[0]
p=1
while p<d:
  p*=2
  e.append(p-1)
e=e[::-1]
for _ in range(int(input())):
  li=list(map(int,input().split()))
  ans1=0
  n1=li[0]+1
  ans2=0
  n2=li[1]+1
  for i in e:
    if (n1-i-1)>=0:
      n1-=i
      n1-=1
      ans1+=1
  ans1+=n1
  for i in e:
    if (n2-i-1)>=0:
      n2-=i
      n2-=1
      ans2+=1
  ans2+=n1
  if(ans1==ans2):
    print(0,0)
  elif ans1>ans2:
    print(2,ans1-ans2)
  else:
    print(1,ans2-ans1)
  

  

