class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        oe = {}
        for l, r, w in edges:       
            if l not in oe:
                oe[l] = set()
            if r not in oe:
                oe[r] = set()
            oe[l].add((r, w))
            oe[r].add((l, w))
        
        def dks(been, c, t):
            cw = been[c]        # Current Weight
            if c not in oe:     # No route to any other city
                return
            pending = set()
            for other, weight in oe[c]:
                ow = weight + cw     # From current city to the other city weight
                if ow > distanceThreshold:
                    continue
                
                if other not in been:
                    been[other] = ow
                    pending.add(other)
                    continue
                if been[other] > ow: # Through this city is more effcient
                    been[other] = ow
                    pending.add(other)

            for o in pending:
                dks(been, o, t)
    
            
        smallest = 0
        mc = n+1
        for city in range(n):
            dv = {city: 0}
            dks(dv, city, distanceThreshold)
            # print(dv)
            cities = len(list(dv.keys())) - 1
            if cities <= mc:
                smallest = city
                mc = cities
        return smallest
        

