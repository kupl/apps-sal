class Solution:
    from collections import Counter
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0] * len(locations)]
        dp[0][start] = 1
        c = dp[0][finish]
        
        for f in range(1, fuel + 1):
            state = [0] * len(locations)
            
            for i, l1 in enumerate(locations):
                for j in range(i + 1, len(locations)):
                    l2 = locations[j]
                    d = abs(l1 - l2)
                    if f - d < 0:
                        continue
                        
                    prev = dp[f - d]
                    state[i] += prev[j]
                    state[j] += prev[i]
            
            dp.append(state)
            c += state[finish]

        return c % (7 + 10 ** 9)
