class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        def dfs(N, K, digit, rst):
            if not N: 
                rst.append(int(''.join(map(str, digit)))); return
            if digit[-1] + K <= 9: 
                dfs(N-1, K, digit + [digit[-1] + K], rst)
            if digit[-1] - K >= 0: 
                dfs(N-1, K, digit + [digit[-1] - K], rst)
        
        if N == 1: return list(range(10))
        if K == 0: return [int(str(i) * N) for i in range(1, 10)]
        rst = []
        for i in range(1, 10):
            dfs(N-1, K, [i], rst)
        return rst

