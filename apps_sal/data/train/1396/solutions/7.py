for i in range(int(input())):
 a,b,c,d=map(int,input().split())
 a-=1
 b-=1
 if a%c==0 and b%d==0:
  print("Chefirnemo")
 elif a!=0 and b!=0 and (a-1)%c==0 and (b-1)%d==0:
  print("Chefirnemo")
 else:
  print('Pofik')
