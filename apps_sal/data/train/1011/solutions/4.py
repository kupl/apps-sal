# cook your dish here
for i in range(int(input())):
 x,y=list(map(int,input().split()))
 z=input()
 c,s=0,0
 for j in z:
  if j.isupper():c+=1
  else:s+=1
 if c<=y and s<=y:
  print('both')
 elif s<=y:
  print('brother')
 elif c<=y:
  print('chef')
 else:
  print('none') 

