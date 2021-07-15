class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        self.ans = 0
        @lru_cache(None)
        def back(curr, fuel):
            aux = 0
            if curr ==finish:
                aux+=1
            for i in range(n):
                if i!=curr:
                    if fuel-abs(locations[curr]-locations[i])>=0:
                        aux+=back(i, fuel-abs(locations[curr]-locations[i]))
            return aux
        return back(start, fuel)%(10**9+7)
        

