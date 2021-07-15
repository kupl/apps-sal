# cook your dish here
try:
 for i in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  if(n&1):
   print("NO")
   continue
  b=n//2
  c=0
  for j in range(b):
   if(l[j]>-1 and l[j+b]>-1 and l[j]!=l[j+b]):
    c=1
    break
   elif(l[j]==l[j+b] and l[j]==-1):
    l[j]=1
    l[j+b]=1
   else:
    if(l[j]==-1):
     l[j]=l[j+b]
    elif(l[j+b]==-1):
     l[j+b]=l[j]
  if(c==1):
   print("NO")
  else:
   print("YES")
   for j in range(n-1):
    print(l[j],end=" ")
   print(l[n-1])
except:
 pass

