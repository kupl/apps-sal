class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        neg = -float(\"inf\")
        cache = [[0] * (n + 1) for _ in range(n + 1)]
        hasCache = [[False] * (n + 1) for _ in range(n + 1)]
        
        def get_result(index, M) -> int:
            if(index == n): 
                return 0
            if hasCache[index][M]:
                return cache[index][M]
            best = neg
            
            for i in range(1, 2*M + 1):
                num = sum(piles[index : index + i])
                score = num - get_result(min(index + i, n), min(max(i, M), n))
                best = max(best, score)
                
            hasCache[index][M] = True
            cache[index][M] = best
            return best
        
        total = sum(piles)
        delta = get_result(0, 1)
        return (total + delta) // 2
