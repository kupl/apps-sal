# cook your dish here
for _ in range(int(input())):
 fin,dis,acc,spe = map(int,input().split())
 tb = fin/spe
 tt = ((2*(fin+dis))/acc)**0.5
 if tt<=tb:
  print('Tiger')
 else:
  print('Bolt')
