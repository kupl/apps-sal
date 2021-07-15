
t=int(input())
for k in range(t):
 n=int(input())
 arr=list(map(int,input().split()))
 set1=[]
 for i in range(n):
  if arr[i] in set1:
   f=1
   print("NO")
   break
  else:
   f=0
   set1.append(arr[i])
  for j in range(i+1,n):
   arr[i]=arr[i]|arr[j]
   if arr[i] in set1:
    f=1
    print("NO")
    break
   else:
    set1.append(arr[i])
    f=0
  if f==1:
   break
 if f==0:
   print("YES")
   
   
   
 
 

