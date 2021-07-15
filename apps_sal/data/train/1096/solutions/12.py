# cook your dish here
import sys
from operator import itemgetter
n, x, y = map(int, input().strip().split())
tests=[]
for _ in range(n):
 start, end = map(int, input().strip().split())
 tests.append([start,end,1+end-start])
start=[]
start[:]=map(int, input().strip().split())
start.sort()
end=[]
end[:]=map(int, input().strip().split())
end.sort()
tests.sort(key=itemgetter(0))
while tests[0][0]<start[0]:
 tests.pop(0)
 n-=1
j=0
for i in range(n):
 while j<x-1 and start[j+1]<=tests[i][0]:
  j+=1
 tests[i][2]+=tests[i][0]-start[j]
tests.sort(key=itemgetter(1))
while tests[-1][1]>end[-1]:
 tests.pop()
 n-=1
j=y-1
for i in range(n-1,-1,-1):
 while j>0 and end[j-1]>=tests[i][1]:
  j-=1
 tests[i][2]+=end[j]-tests[i][1]
minimo=tests[0][2]
for i in range(n):
 minimo=min(minimo, tests[i][2])
print(minimo)
