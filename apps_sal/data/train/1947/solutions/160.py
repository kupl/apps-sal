from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        bcounter = Counter()
        
        for b in B:
            bbc = Counter(b)
            for c in bbc:
                if c not in bcounter or bbc[c] > bcounter[c]:
                    bcounter[c] = bbc[c]
        
        ans = []
        for a in A:
            aac = Counter(a)
            uni = True
            for c in bcounter:
                if c not in aac or aac[c] < bcounter[c]:
                    uni = False
                    break
            if uni: ans.append(a)
        return ans
            

