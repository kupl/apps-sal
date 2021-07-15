for _ in range(int(input())):
 n=int(input())
 h=[0]+[int(i) for i in input().split()]+[0]
 l=[0]*(n+2)
 r=[0]*(n+2)
 for i in range(1,n+1):
  l[i]=min(l[i-1]+1,h[i])
 for i in range(n,0,-1):
  r[i]=min(r[i+1]+1,h[i])
 maxi=0 
 for i in range(n):
  curr=min(l[i],r[i])
  maxi=max(maxi,curr)
 print(sum(h)-maxi*maxi)

