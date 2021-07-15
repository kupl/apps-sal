# cook your dish here
def sol(arr,n,k):
 m=-1
 for i in range(n):
  flag=0
  count=1 
  s=set()
  s.add(arr[i])
  temp=i
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
 return m
 
test=int(input())
for _ in range(test):
 n,k = map(int,input().split())
 arr = list(map(int,input().split()))
 if k==2:
  mi=sol(arr,n,k)
  print(mi)
  continue
 freq=[0]*n
 i=0
 j=0
 c=0
 l=0
 mx=-1
 k-=1
 for x in range(n):
  freq[arr[x]]+=1 
  if freq[arr[x]]==1:
   c+=1 
  while(c>k):
   freq[arr[l]]-=1
   if freq[arr[l]]==0:
    c-=1
   l+=1 
  if x-l+1>=j-i+1:
   j=x
   i=l
 print(j-i+1)
