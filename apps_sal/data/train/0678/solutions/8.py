# cook your dish here
for _ in range(int(input())):
 a=int(input())
 arr=list(map(int,input().split()))
 i=1
 last=0
 max1=1
 sum1=0
 while(True):
  sum1+=sum(arr[last:max1])
  last=max1
  max1=sum1+last
  if(max1>=(a)):
   break
  else:
   i+=1
 print(i)



