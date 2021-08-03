class Solution:
    \"\"\"
    S(i, i, 0) = 1
    |F| * |V| 
    S(start, j, f) = \\sum for k in |V|  S(start, k, f-d); d = |k - j|  
    \"\"\"
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        
        # S[fuel][end]
        dp = [[0 for _ in range(N)] for _ in range(fuel+1)]
        
        # Base case
        dp[0][start] = 1
        
        for f in range(1, fuel+1):
            for k in range(N):
                for j in range(k+1, N): 
                    d = abs(locations[k] - locations[j])
                    if d > f: 
                        continue
                    add_k, add_j = dp[f-d][k], dp[f-d][j]
                    dp[f][j] += add_k
                    dp[f][k] += add_j
                    dp[f][j] %= int(1e9) + 7
                    dp[f][k] %= int(1e9) + 7
        print(dp)
        
        return sum(dp[f][finish] for f in range(len(dp))) % (int(1e9) + 7)
