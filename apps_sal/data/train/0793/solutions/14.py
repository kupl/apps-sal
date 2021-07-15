# cook your di
import math
n,r=map(int,input().split())
l=list(map(int,input().split()))
ans=0
for i in range(len(l)):
    ans=math.gcd(ans,abs(l[i]-r))
print(ans)
