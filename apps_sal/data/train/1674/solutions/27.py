class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        self.len = l
        dp = {}
        
        total = sum(piles)
        
        maxDiff = self.help(piles, 0, 1, dp)
    
        return int((total+ maxDiff)/2)
    
    def help(self, piles, index, m, dp):
        
        if index >= self.len:
            return 0
        
        if dp.get((index, m)) != None:
            return dp.get((index,m))
        
        res = -0xFFFFFFF
        s = 0
        for i in range(index, self.len):
            if i - 2*m >= index:
                break
            s += piles[i]
            res = max(res, s - self.help(piles, i+1, max(m, i - index + 1), dp))
        
        dp[(index, m)] = res
        
        return res
