# cook your dish here
ans=[]
for test in range(int(input())):
 n=int(input())
 arr=list(map(int,input().split()))
 m=0
 s=set(arr)
 for i in s:
  if arr.count(i)>m:
   m=arr.count(i)
 ans.append(n-m)
for i in ans:
 print(i)

