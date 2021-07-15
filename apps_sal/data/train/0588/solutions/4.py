# cook your dish here
from functools import reduce
from math import gcd
for _ in range(int(input())):
 num=int(input())
 cuts=list(map(int,input().split(" ")))
 initial_cuts=[0]*(num-1)
 for i in range(0,num-1):
  
  initial_cuts[i]=cuts[i+1]-cuts[i]
 initial_cuts.append(360) 
 red=reduce(gcd,initial_cuts)
 total_initial=int(360/red)
 vasya_cuts=total_initial-num
 print(vasya_cuts)
