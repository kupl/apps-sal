# cook your dish here
t=int(input())
for _ in range(t):
 n,m = map(int,input().split())
 count=0
 for i in range(n,m+1):
  p=str(i)
  if p[-1]=='2' or p[-1]=='3' or p[-1]=='9':
   count+=1
 print(count)
