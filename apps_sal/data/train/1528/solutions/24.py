t=int(input())
for i in range(t):
 n,k=list(map(int,input().split()))
 arr = list(map(str,input().strip().split()))[:n] 
 l=[]
 counter=0
 for i in range(len(arr)):
  if(arr[i] == "H"):
   l.append(1)
  else:
   l.append(0)
 for i in range(n-1,n-k-1,-1):
  if(l[i] == 0):
   counter+=1
   continue
  else:
   for j in range(i):
    if(l[j]==1):
     l[j]-=1
    else:
     l[j]+=1
   counter+=1
   if(counter == k):
    break
 head=0
 for k in range(n-k):
  if l[k]==1:
   head+=1
 print(head)

