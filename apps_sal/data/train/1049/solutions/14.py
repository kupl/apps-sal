def f():
 n,k=list(map(int,input().split()))
 a=list(map(int,input().split()))
 distinctitem=len(set(a))
 count=[0]*1000000
 temp=[]
 maxi=0
 s=0
 c=0
 for i in range(0,len(a)):
  if len(temp)<k:
   temp.append(a[i])
   if count[a[i]]==0:
    count[a[i]]+=1
    c+=1
    s+=a[i]
   else:
    count[a[i]]+=1
    s+=a[i]
  #print(temp,s)
  if len(temp)==k:
   if c==distinctitem:
    maxi=max(maxi,s)
   s-=temp[0]
   count[temp[0]]-=1
   if count[temp[0]]==0:
    c-=1
   temp.pop(0)
  
 print(maxi)
for i in range(int(input())):
 f()
    
  

