a=list(map(float,input().split()))
a.sort()
if(a[0]/a[1]==a[2]/a[3]):
  print('Possible')
else:
  print('Impossible')
