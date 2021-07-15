from numpy import *
input()
a=array(input().split(),dtype=int)
d=a-minimum.accumulate(a)
print((d==d.max()).sum())
