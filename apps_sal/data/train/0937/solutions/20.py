for _ in range(int(input())):
 
 s=''
 x=input()
 y=list(x)
 y.sort()
 for i in y:
  s+=i
 
 #print(s,x)
 
 if(s==x):
  
  print('yes')
  
 else:
  
  print('no')
