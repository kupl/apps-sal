
from itertools import permutations
    
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        arr = sorted(arr, reverse=True)
        
        perms = permutations(arr)
        
        for perm in perms:
            m = perm[0] * 10 + perm[1]
            s = perm[2] * 10 + perm[3]
            
            if m < 24 and s < 60:
                strm = str(m)
                strs = str(s)
                if len(strm) < 2:
                    strm = \"0\" + strm
                if len(strs) < 2:
                    strs = \"0\" + strs
                return \"{}:{}\".format(strm, strs)
        
        return \"\"
