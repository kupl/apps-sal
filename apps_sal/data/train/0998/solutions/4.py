from sys import stdin,stdout
from math import gcd,log2,log10,floor;
import math;
from collections import defaultdict,OrderedDict
from bisect import bisect_left
# import numpy as np
# input=stdin.readline
# print=stdout.write

n,q=list(map(int,input().split()))

r=[0]*(n+1);
c=[0]*(n+1);
for i in range(q):
 alpha,beta,gamma=list(map(str,input().split()))
 beta,gamma=int(beta),int(gamma)
 if alpha=="RowAdd":
  r[beta]+=gamma;
 else:
  c[beta]+=gamma;
print(max(r)+max(c))


