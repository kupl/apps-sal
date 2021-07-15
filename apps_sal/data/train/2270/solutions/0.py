# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,X,Y,Z = list(map(int,read().split()))

N = 1<<(X+Y+Z)
NX = 1<<X
NY = 1<<(X+Y)
NZ = 1<<(X+Y+Z)

MX = (1<<X) - 1
MY = (1<<(Y+X)) - (1<<X)
MZ = (1<<(X+Y+Z)) - (1<<(Y+X))

MMX = MX<<1
MMY = MY<<1
MMZ = MZ<<1

dp = [0]*N
dp[1] = 1

MOD = 10**9+7

for _ in range(n):
    ndp = [0]*N
    #cnt = 0
    #bad = 0
    for mask in range(N):
        if dp[mask]==0: continue
        mx = mask&MX
        my = mask&MY
        mz = mask&MZ
        
        for j in range(1,11):
            nmx = mx << j
            nmx &= MMX

            nmy = my << j
            nmy &= MMY

            nmz = mz << j
            nmz &= MMZ

            nmask = nmx|nmy|nmz|1
            if not nmask&(1<<(X+Y+Z)):
                ndp[nmask] += dp[mask]
                ndp[nmask] %= MOD

    dp = ndp
    #print(sum(dp),"sum")

ans = (pow(10,n,MOD)-sum(dp))
print((ans%MOD))



