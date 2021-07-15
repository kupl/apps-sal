
t = int(input())
for _ in range(t):
 n,k = list(map(int,input().split()))

 l = list(map(int,input().split()))
 l.sort()
 a = max(sum(l[k:])-sum(l[:k]),sum(l[:k])-sum(l[k:]))
 l.sort(reverse=True)
 b = max(sum(l[k:])-sum(l[:k]),sum(l[:k])-sum(l[k:]))
 print(max(a,b)) 



