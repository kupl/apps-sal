t=int(input())
for _ in range(t):
 n,l,r=list(map(int,input().split()))
 lr=[1]
 ll=[1]
 for i in range(1,r):
  lr.append(2**i)
 for i in range(1,l):
  ll.append(2**i)
 if(len(lr)!=n):
  for i in range(n-r):
   lr.append(lr[-1])
 if(len(ll)!=n):
  for i in range(n-l):
   ll.append(ll[0])
 print(sum(ll),sum(lr))

