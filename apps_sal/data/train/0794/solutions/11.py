import sys
import math
from collections import defaultdict, Counter

# input=sys.stdin.readline
# def print(x):
#     sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP3/output.txt",'w')
# sys.stdin=open("CP3/input.txt",'r')

m = pow(10, 9) + 7
t = int(input())
for i in range(t):
    n, m1 = map(int, input().split())
    a = list(map(int, input().split()))
    if m1 == n - 1:
        ans = 1
        c = Counter(a)
        for j in c:
            if j == 1:
                continue
            ans = (ans * pow(c.get(j - 1, 0), c[j], m)) % m
        #   if c[j]>c.get(j-1,0):
        #       ans=0
        #       break
        #   cur=1
        #   for k in range(c[j-1],c[j-1]-c[j],-1):
        #       cur=(cur*k)%m
        #   ans=(ans+cur)%m
        # if max(c)==1:
        #   ans=1
        print(ans)
    else:
        print(0)
