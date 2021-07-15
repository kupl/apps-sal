#

for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 arr = list(map(int,input().split()))
 m=-1
 for i in range(n):
  flag=0
  count=1 
  s=set()
  s.add(arr[i])
  for j in range(i+1,n):
   if arr[j] not in s:
    if len(s)==k-1:
     flag=1
    else:
     s.add(arr[j])
     count+=1 
   else:
    count+=1
   if flag==1:
    break
  if count>m:
   m=count
 print(m)
    
    
    
   

