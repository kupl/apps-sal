from functools import *
class Solution:
    def stoneGameII(self, arr):
        a =[]
        s=0
        n = len(arr)
        for i in arr[::-1]:
            s+=i
            a.append(s)
        a=a[::-1]
        @lru_cache(None)
        def fun(i,m):
            if i+2*m>=n:return a[i]
            mn = inf
            for ii in range(1,2*m+1):
                if ii>m:
                    ans = fun(i+ii,ii)
                else:
                    ans=fun(i+ii,m)
                if ans<mn:
                    mn = ans
            return a[i]-mn
        return fun(0,1)
                
            

