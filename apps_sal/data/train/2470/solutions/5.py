class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i] = tuple(sorted(dominoes[i]))
            
        ans = 0
        
        for i in set(dominoes):
            d = dominoes.count(i)
            if d > 1:
                ans += d*(d-1) // 2
        return ans
