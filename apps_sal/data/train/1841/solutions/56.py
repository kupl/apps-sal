class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        s = sorted(arr)
        i = (len(arr)-1)//2
        m = s[i]
        
        strengths = []
        
        for item in s:
            st = abs(item-m)
            strengths.append((st, item))
        
        sorted_strengths = sorted(strengths, reverse=True)
        sorted_vals = []
        
        for ss in sorted_strengths:
            sorted_vals.append(ss[1])
            
        return sorted_vals[:k]
        

