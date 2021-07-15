t = int(input())
for i in range(t):
 N,K,V=map(int,input().split())
 l=list(map(int,input().split()))
 sum1 = (N+K)*V - sum(l)
 avg = sum1/K
 avg1 = sum1//K
 if(avg==avg1 and avg>=1):
  print(avg1)
 else:
  print("-1")
