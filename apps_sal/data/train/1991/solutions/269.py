class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7
        return self.dfs(locations, start, finish, fuel, {}) % mod
        
      
    def dfs(self, locations, start, finish, fuel, memo):
      if (start, fuel) in memo:
        return memo[(start, fuel)]
      if fuel < 0:
        return 0
      count = 0
      if start == finish: 
        count += 1
        
      for i in range(len(locations)):
        diff = abs(locations[i] - locations[start])
        if i == start:
          continue
        count += self.dfs(locations, i, finish, fuel - diff, memo)
      memo[(start, fuel)] = count % (10**9+7) 
      return memo[(start, fuel)]
