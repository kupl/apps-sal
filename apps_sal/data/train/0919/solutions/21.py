for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 l=0
 d=[]
 for i in range(n+1):
  d.append(-1)
 for i in a:
  l,d[i]=max(l,d[i]+1),max(d[i],l+1)
 print(n-l)
     

