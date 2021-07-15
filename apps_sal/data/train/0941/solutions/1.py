# cook your dish here
import math;
t=int(input())
for i in range(t):
 (a,b)=tuple(map(int,input().split()))
 ea=a//2;
 eb=b//2;
 oa=math.ceil(a/2);
 ob=math.ceil(b/2);
 print(ea*eb+oa*ob)

