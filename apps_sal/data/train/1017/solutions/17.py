# cook your dish here
for _ in range(int(input())):
 l=list(map(int,input().split()))
 l=(sum(l)-l[5])*l[5]
 if(l<=(24*5)):
  print('No')
 else:
  print('Yes')

