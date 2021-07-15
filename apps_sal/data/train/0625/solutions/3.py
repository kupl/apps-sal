import atexit
import io
import sys
import math
from collections import defaultdict,Counter

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# sys.stdout=open("CP2/output.txt",'w')
# sys.stdin=open("CP2/input.txt",'r')

m=pow(10,9)
t=int(input())
for i in range(t):
    n=int(input())
    d={0:1}
    a=list(map(int,input().split()))
    s=0
    ans=0
    for j in a:
        s+=j
        need=s%m
        ans+=d.get(need,0)
        s1=d.setdefault(s%m,0)
        d[s%m]+=1
    print(ans)
