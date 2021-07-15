# cook your dish here
for _ in range(int(input())):
 n,m,s=list(map(int,input().split()))
 arr=list(map(int,input().split()))
 arr.sort()
 count=0
 for a in arr:
  if a<=s and m>=1:
   count+=1
   m-=1
  elif a<=2*s and m>=2:
   count+=1
   m-=2
 print(count)

