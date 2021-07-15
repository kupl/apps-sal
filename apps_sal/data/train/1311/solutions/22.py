for _ in range(int(input())):
 N,K=map(int,input().split())
 po=K
 ne=N-K
 arr=[]
 cumsum=0
 coupo=0
 coune=0
 for i in range(N):
  if coupo==K:
   arr.append(-(i+1))
   coune+=1
   continue
  elif coune==ne:
   arr.append(i+1)
   coupo+=1
   continue
  a=cumsum+(i+1)
  b=cumsum-(i+1)
  if abs(a)>abs(b):
   cumsum=b
   arr.append(-(i+1))
  else:
   cumsum=a
   arr.append(i+1)
  if cumsum>0:
   coupo+=1
  else:
   coune+=1
 for i in range(len(arr)):
  print(arr[i],end=" ")
  
  
  

