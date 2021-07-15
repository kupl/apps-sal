#!/usr/bin/python
# coding: utf-8

t=int(input())
for i in range(t):
 (n,d)=list(map(int,input().split(' ')))
 arr=list(map(int,input().split(' ')))
 sum=0
 for j in arr:
  sum+=j
 if((sum%n)!=0):
  print("-1")
 else:
  tmp=0
  avg=sum/n
  num=[0]*d
  cnt=[0]*d
  for j in range(n):
   num[j%d]+=arr[j]
   cnt[j%d]+=1
  for j in range(d):
   if(num[j]%cnt[j]!=0 or num[j]/cnt[j]!=avg):
    tmp=1
    break
  if(tmp):
   print("-1")
  else:
   ans=0
   for j in range(n):
    if(arr[j]<avg):
     tmp=avg-arr[j]
     ind=j+d
     if(ind<n and arr[ind]>0):
      ans+=tmp
      arr[j]=avg
      arr[ind]-=tmp
    elif(arr[j]>avg):
     tmp=arr[j]-avg
     ind=j+d
     if(ind<n):
      ans+=tmp
      arr[j]=avg
      arr[ind]+=tmp
   print(ans)

