big = 1000000007
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        if fuel < abs(locations[start] - locations[finish]): return 0
        buf, idx = {(finish, 0): 1}, set(range(len(locations)))
        found = buf.get((start, 0), 0)
        for n in range(1, fuel):
            for i in idx:
                now = sum([ buf.get((j, n - abs(locations[i] - locations[j])), 0)
                           for j in idx - {i} ])
                if now: buf[i,n] = now
            if (start, n) in buf: found = (found + buf[start,n]) % big
        found += sum([ buf.get((j, fuel - abs(locations[start] - locations[j])), 0) 
                      for j in idx - {start} ])
        return found % big
