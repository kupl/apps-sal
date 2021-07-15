compu=[(x*(x+1),x) for x in range(1,316)]
t=int(input())
for i in range(t):
 s=list(map(int,input().strip()))
 count=0
 #find prefix sum of 0s
 arr=[0]
 n=len(s)
 for i in range(1,n+1):
  arr.append(arr[i-1]+s[i-1])
 for i,a in compu:
  #count first i length substring
  if(i>n):
   break
  s1=arr[i]
  s0=i-s1
  if(s0==s1*s1):
   count+=1
  j=1
  while(j<(n-i+1)):
   s1=arr[i+j]-arr[j]
   s0=i-s1
   if(s0==s1*s1):
    count+=1
    j+=1
   else:
    j+=abs(a-s1)
 print(count)
