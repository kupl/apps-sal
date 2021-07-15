t = int(input())

for _ in range(t):
 N, D = list(map(int, input().split()))
 L = list(map(int, input().split()))
 flag = True
 avg = None
 for x in range(D):
  temp = x
  sumA = L[x]
  numElem = 1
  while temp+D<N:
   numElem+=1
   sumA+=L[temp+D]
   temp+=D
   
  if sumA%numElem:
   flag = False
   break
   
  
  if avg==None:
   avg = sumA/numElem
  elif avg!=(sumA/numElem):
   flag = False
   break
   
  
 if flag:
  res = 0
  tempDiff = 0
  for x in range(D):
   temp = x 
   tempDiff = L[x]-avg
   while temp+D<N:
    L[temp+D]+=tempDiff
    if tempDiff<0:
     res-=tempDiff
    else:
     res+=tempDiff
    temp+=D
    tempDiff = L[temp]-avg
    
  print(res)
    
 else:
  print(-1)
