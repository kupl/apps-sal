class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        for i in range(len(dominoes)):
            dominoes[i] = tuple(sorted(dominoes[i]))
        ans = 0
        for i in set(dominoes):
            t = dominoes.count(i)
            ans += t*(t-1)//2
        return ans
