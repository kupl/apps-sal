class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        n = len(A)
        memo = {}
        def take(i, m, alex):
            if i >= len(A):
                return 0
            
            if (i, m, alex) in memo:
                return memo[(i, m, alex)]
            
            if alex:
                res = 0
                taking = 0
                for x in range(1, min(n,2*m + 1)):
                    if i+x-1 < n:
                        taking += A[i+x-1]
                    res = max(res, taking + take(i+x, max(m, x), False))
            else:
                res = sum(A[i:])
                for x in range(1, min(n,2*m + 1)):
                    res = min(res, take(i+x, max(m,x), True))
            
            memo[(i, m, alex)] = res
            
            return res
        return take(0, 1, True)
                
                
                    

