for i in range(int(input())):
 a,b=list(map(int,input().split())) 
 ar=list(map(int,input().split())) 
 for j in ar:
  if j>=b:
   print('YES')
   break
 else:
  print('NO')

