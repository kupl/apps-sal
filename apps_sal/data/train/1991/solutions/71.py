class Solution:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        def dfs(index,current_fuel):
            if not current_fuel and index==finish: return 1
            paths=index==finish
            for i,n in enumerate(locations):
                if i==index: continue
                tmp_fuel=current_fuel-abs(locations[index]-n)
                if (i,tmp_fuel) in memo: paths+=memo[(i,tmp_fuel)]
                elif tmp_fuel>=0:paths+=dfs(i,tmp_fuel)
            memo[(index,current_fuel)]=paths
            return paths
        memo={}
        return dfs(start,fuel)%(10**9+7)
