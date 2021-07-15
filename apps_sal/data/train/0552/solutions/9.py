# cook your dish here
for x in range(int(input())):
 n,k=input().split()
 n=int(n)
 k=int(k)
 l=list(map(int,input().split()))
 l.sort()
 if k<=n//2:
  print(sum(l[k:])-sum(l[:k]))
 else:
  print(abs(sum(l[:n-k])-sum(l[n-k:])))
  

