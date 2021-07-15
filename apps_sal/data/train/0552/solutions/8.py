def solve():
 n,k=map(int,input().split())
 w=list(map(int,input().split()))
 if k<=n//2:
  w.sort()
 else:
  w.sort(reverse=True)
 print(abs(sum(w[k:])-sum(w[:k])))

t=int(input())
while t:
 solve()
 t-=1
