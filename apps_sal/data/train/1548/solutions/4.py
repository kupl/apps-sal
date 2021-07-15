for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 left=[]
 mini=float('inf')
 for i in range(n):
  c=min(mini+1,l[i])
  left.append(c)
  mini=c
 mini=float('inf')
 for i in range(n-1,-1,-1):
  left[i]=min(mini+1,left[i])
  mini=min(mini+1,l[i])
 print(*left)
