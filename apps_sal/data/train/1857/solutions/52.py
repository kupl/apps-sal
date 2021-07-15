import numpy as np
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d, ans = defaultdict(set), 0
        for r,c in reservedSeats:
            d[r].add(c)
        absent = lambda x,s: not any(filter(lambda x: x in s, range(x,x+4)))
        for _,v in d.items():
            ans+= 1+absent(6,v) if absent(2,v) else (absent(4,v) or absent(6,v))
        ans+=2*(n-len(d))
        return ans
