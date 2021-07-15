# cook your dish here
t=int(input())
for _ in range(t):
 n=int(input())
 s=list(map(int,input().split()))
 
 s.sort(reverse=True)
 cnt=0
 
 for i in range(0,n,2):
  cnt += s[i]
  
 print(cnt)
