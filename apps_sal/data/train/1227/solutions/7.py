for _ in range(int(input())):
 a = input().split()
 y = 0
 if(a[4]==a[0]==a[3]):
  y=1
 elif(a[4]==a[0]==a[2]):
  y=1
 elif(a[4]==a[1]==a[3]):
  y=1
 elif(a[4]==a[1]==a[2]):
  y=1
 elif(a[5]==a[0]==a[3]):
  y=1
 elif(a[5]==a[0]==a[2]):
  y=1
 elif(a[5]==a[1]==a[3]):
  y=1
 elif(a[5]==a[1]==a[2]):
  y=1
 if(y==1):
  print("YES") 
 else:
  print("NO") 
 

