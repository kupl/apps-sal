t=int(input())
while(t>=1):
  t-=1
  a=int(input())
  if(a==1):
    print(1)
    print(*[1,1])
  else:
    print(a//2)
    for i in range(a//2-1):
      print(*[2,i*2+1,i*2+2])
    if(a%2==0):
      print(*[2,a-1,a])
    else:
      print(*[3,a-2,a-1,a])
 
