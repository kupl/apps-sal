# cook your dish here
import math as m
tst,N = list(map(int,input().split()))
for i in range(tst):
 val = int(input())
 #z = m.floor(z)
 s = int(m.sqrt(val))
 S = pow(s,2)
 p = val-S
 q = int((N*val)*(.01))
 if p<=q:
  print("yes")
 else:
  print("no")


