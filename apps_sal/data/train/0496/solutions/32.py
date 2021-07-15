from collections import Counter
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        c=Counter(A)
        prev=-1
        ans=0
        for key in sorted(c):
            if key<=prev:
                ans+=(0+c[key]-1)*c[key]//2+c[key]*(prev-key+1)
                prev=key+c[key]-1+prev-key+1
            else:
                ans+=(0+c[key]-1)*c[key]//2
                prev=key+c[key]-1
        return ans
