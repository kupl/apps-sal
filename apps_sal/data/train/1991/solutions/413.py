from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.cities = set()
        self.seen = defaultdict(int) 
        self.maxl = 0
    
    def countways(self, start, curfuel, finish):
        if start == finish:
            if (start, curfuel) in self.seen:
                return 1 + self.seen[(start, curfuel)]
            elif curfuel > 0:
                self.seen[(start, curfuel)] = 0
                for x in range(len(self.cities)):
                    if not x == start:
                        cost = abs(self.cities[x] - self.cities[start])
                        if curfuel - cost >= 0:
                            self.seen[(start, curfuel)] += self.countways(x, curfuel-cost, finish) 
            return 1 + self.seen[(start, curfuel)]
        elif curfuel <= 0:
            return 0
        elif (start, curfuel) in self.seen:
            return self.seen[start, curfuel]
        else:
            self.seen[(start, curfuel)] = 0
            for x in range(len(self.cities)):
                if not x == start:
                    cost = abs(self.cities[x] - self.cities[start])
                    if curfuel - cost >= 0:
                        self.seen[(start, curfuel)] += self.countways(x, curfuel-cost, finish) % (1e9+7)
                
            return self.seen[(start, curfuel)] % (1e9+7)

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        self.cities = locations
        return int(self.countways(start, fuel, finish) % (1e9+7))
