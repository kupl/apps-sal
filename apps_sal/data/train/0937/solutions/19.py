# cook your dish here
for _ in range(int(input())):
 s=''
 x=input()
 y=list(x)
 y.sort()
 for i in y:
  s+=i
 if(s==x):
  print("yes")
 else:
  print("no")
