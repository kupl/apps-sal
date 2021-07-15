for h in range(int(input())):
 n,m = map(int , input().split())
 l=list(map(int,input().split()))
 s=min(l)
 b=max(l)
 l1=[]
 for i in range(n):
  l1.append(max(abs(i-s),abs(i-b)))
 print(*l1)
