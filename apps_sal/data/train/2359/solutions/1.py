

import numpy as np
from numba import njit
@njit
def main(n,k,mod):
    l=k*(n*(n+1))//2
    dp=np.zeros((n+1,l+1),dtype=np.int32)
    # dp[i][j]:iまでの数字を使い、合計がjになるものの個数
    # O(N^3*k)<=O(10^8)で計算可能らしい
    dp[0,0]=1
    ary=np.ones((1,l+2),dtype=np.int32)
    ary[0,0]=0
    for i in range(1,n+1):
        nary=np.zeros((i+1,2+l//i),dtype=np.int32)
        for j in range(l+1):
            a=j//i
            b=max(0,j//i-k)
            dp[i,j]=ary[j%i,a+1]-ary[j%i,b]
            dp[i,j]%=mod
            nary[j%(i+1),j//(i+1)+1]=dp[i,j]
            nary[j%(i+1),j//(i+1)+1]+=nary[j%(i+1),j//(i+1)]
            nary[j%(i+1),j//(i+1)+1]%=mod
        ary=nary
    ret=[]
    for i in range(1,n+1):
        # 左区間=[1,i-1]
        # 右区間=[1,n-i]
        ans=0
        num=dp[i-1,0]
        num*=dp[n-i,0]
        ans+=num*k
        ans%=mod
        for j in range(1,l+1):
            num=dp[i-1,j]
            num*=dp[n-i,j]
            num%=mod
            ans+=(num*(k+1))%mod
            ans%=mod
        ret.append(ans)
    #for x in ret:
    #    print(x)
    return ret

n,k,mod=map(int,input().split())
print(*main(n,k,mod),sep='\n')
