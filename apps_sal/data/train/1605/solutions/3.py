'''
Created on Oct 12, 2014

@author: Ismael
'''

#import time

MOD = 10**9+7
def sumTermsArith1(firstTerm,r,nbTerms):
    return (nbTerms*(2*firstTerm+(nbTerms-1)*r))//2

def solve(a,b):
    s = 0
    for rem in range(1,b):
        reason = rem*b
        s = (s+sumTermsArith1(reason+rem,reason,a))%MOD
    return s

def solve2(a,b):
    reason = a*(b*(a+1)+2)//2
    return sumTermsArith1(reason,reason,b-1)%MOD

#t = time.clock()
a,b = list(map(int,input().split()))
#sol1 = solve(a,b)
sol2 = solve2(a,b)
print(sol2)
#print(sol1 == sol2)
#print(time.clock()-t)

