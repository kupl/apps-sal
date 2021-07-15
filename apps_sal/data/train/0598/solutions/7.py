k1=input()
k1=list(map(int,k1.split(" ")))
k=k1[1]
ar=input()
ar=list(map(int,ar.split(" ")))
if(k==0):
 for i in ar:
  print(i, end=' ')
elif(k%2==1):
 max1=max(ar)
 for i in range(0,len(ar)):
  ar[i]=max1-ar[i]
 for i in ar:
  print(i, end=' ')
else: 
 for l in range(0,2):
  max1=max(ar)
  for i in range(0,len(ar)):
   ar[i]=max1-ar[i]
 for i in ar:
  print(i, end=' ')
