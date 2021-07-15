test=int(input())
for _ in range(test):
 a=int(input())
 flag=0
 r=0
 if a==1:
  print('2')
 elif a&(a+1)==0:
  print(a//2)
 else:
  print('-1')
