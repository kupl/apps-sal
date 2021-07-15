# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,r,*a = list(map(int,read().split()))


high = a[-1]
delta = -1

for ai in a[::-1]:
    if high < ai:
        high = ai
    if high-ai > delta:
        delta = high-ai

#from collections import Counter
#d = Counter()

high = a[-1]

hs = 0
ls = 0

ans = 0
for ai in a[::-1]:
    if high < ai:
        high = ai
        hs = 1
        ans += min(hs,ls)
        ls = 0
    elif high == ai:
        hs += 1        
    
    if high - ai == delta:
        ls += 1
    

print((ans+min(hs,ls)))





