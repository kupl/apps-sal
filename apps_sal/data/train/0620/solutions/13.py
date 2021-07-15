t=int(input())
while(t>0):
 n,k=[int(x) for x in input().split()]
 a=[int(x) for x in input().split()]
 first=0
 prev=0
 i=0
 len=0
 maxlen=0
 while(i<n):
  if(a[i]>k):
   if(first==0):
    first=a[i]
    prev=i
    len+=1
   else:
    if(first==a[i]):
     len+=1
     prev=i
    else:
     first=0
     i=prev
     if(maxlen<len):
      maxlen=len
     len=0
  else:
   len+=1
  i+=1
 else:
  if(maxlen<len):
   maxlen=len
 print(maxlen)
 t-=1

