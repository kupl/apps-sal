class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        import itertools
        ret = ''
        for a, b, c, d in itertools.permutations(arr):
            h = a*10 + b
            m = c*10 + b
            if h >= 24 or m >59:
                continue
                
            t = f\"{a}{b}:{c}{d}\"
            if not ret:
                ret = t
            else:
                ret = max(ret, t)
        return ret            
                
