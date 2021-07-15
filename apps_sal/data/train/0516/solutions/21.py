#!/usr/bin/env python
import os
import sys

def main():
    t = int(input())
    
    while t>0:
        n,k = map(int,input().split())
        l = list(map(int,input().split()))
        
        ll = sorted(l)
        count1 = 0
        
        for i,val in enumerate(ll):
            count1 = count1 + ( i - (ll[:i]).count(val) )
        
        ans = 0
        
        ans = ans + ( count1 * k * (k-1) ) // 2
        
        count2 = 0
        
        for i,val in enumerate(l):
            temp = sum( 1 for j in l[i+1:] if j < val)
            count2 = count2 + ( temp )
        
        ans = ans + count2*k
        
        sys.stdout.write(str(ans)+"\n")
        t-=1
    
def __starting_point():
    main()
__starting_point()
