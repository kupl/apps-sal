import math
for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 gc=a[0]
 for i in a :
  gc=math.gcd(gc,i)
 print(gc,sum(a)//gc)
