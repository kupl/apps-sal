class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # no solution for 1
        if n == 1:
            return []
        
        ans = []
        seen = set()
        for i in range(2, n+1):
            denom = str(i)
            for j in range(1, i):
                result = j/i
                if result in seen:
                    continue
                ans.append(str(j)+\"/\"+denom)
                seen.add(result)
        return ans
        
