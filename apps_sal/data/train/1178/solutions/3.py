# cook your dish here
t=int(input())
for _ in range(t):
 n = int(input())
 
 a = list(map(int,input().split()))
 a.sort()
 cnt=0
 
 for i in range(n):
  
  if cnt<a[i]:
   break
  
  else:
   cnt+=1
   
 print(cnt)
