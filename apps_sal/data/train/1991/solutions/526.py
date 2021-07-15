class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        DP = [[0] * len(locations) for _ in range(fuel + 1)]
        
        DP[fuel][start] = 1
        
        for i in range(fuel - 1, -1, -1):
            for j in range(len(locations)):
                
                for k in range(len(locations)):
                    
                    if j == k:
                        continue
                    past = i + abs(locations[k] - locations[j])
                    if past > fuel:
                        DP[i][j] += 0
                    else:
                        DP[i][j] += DP[past][k]
        
        
        return sum(row[finish] for row in DP) % (10**9 + 7)
