MIN = float('-inf')
class Solution:
    def stoneGameII(self, piles):
        
        def dfs(start, M, memo):
            if start == len(piles):
                return 0
            if (start,M) in memo:
                return memo[(start,M)]
            max_diff = MIN
            for X in range(1, 2*M+1):
                cur, end = 0, min(len(piles), start+X)
                for i in range(start, end):
                    cur += piles[i]
                max_diff = max(max_diff, cur-dfs(end, max(M,X), memo))
            memo[(start,M)] = max_diff
            return max_diff
        
        total = sum(piles)
        return (dfs(0, 1, {})+total) // 2
        

