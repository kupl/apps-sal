import math
import random
import re
import os
import sys
def cake(c):
    k=c[2]
    t=c[3]
    s=0
    for i in range(c[1]):
      s+=k
      k*=t
    if s>c[0]:
      s-=c[0]
      c.append("IMPOSSIBLE")
      c.append(-s)
    else:
      s=c[0]-s
      c.append("POSSIBLE")
      c.append(s)
    return (list(str(c[4])+str(c[5]))) 
def main():
    n = int(input())
    c=[[]]*n
    res=[]
    m=[]
    cou=0
    for i in range(n):
      c[i] = list(map(int, input().rstrip().split()))
      res.append(cake(c[i]))
    for i in range(len(c)):
        print(*c[i][-2:-1], end=" ")
        print(abs(*c[i][-1:]))
        m.append(*c[i][-1:])
    cou=sum(m)
    if cou>0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    return 0
def __starting_point():
    main()

__starting_point()
