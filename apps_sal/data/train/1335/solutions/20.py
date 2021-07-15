import math
N = list(map(int,input().strip().split()))
A=list(map(int,input().strip().split()))
#print(set(A))
b=0
c=0
d=0
for j in set(A):
 b=math.ceil(A.count(j)/2)
 d+=b
 #print(b,d,c)
print(d+c)

