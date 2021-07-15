# 1575. Count All Possible Routes

MOD = 10**9 + 7

def gen_matrix (m, n, elem):
    return [[elem for col in range (n)] for row in range (m)]

def count_routes (cities, start, finish, fuel):
    m_routes = gen_matrix (fuel + 1, len (cities), None)

    def dist (c1, c2):
        return abs (cities[c1] - cities[c2])

    def routes (f, c):
        '''Number of routes *to reach* finish with fuel f
        starting from city c'''

        if f < 0:
            return 0

        if m_routes[f][c] is not None:
            return m_routes[f][c]

        if f == 0 and c != finish:
            # cannot reach city now
            ans = 0
        else:
            current_sol = bool (c == finish)
            ans = current_sol + sum (routes (f - dist (c, c2), c2) for c2 in range (len (cities)) if c2 != c)
            ans %= MOD
        
        m_routes[f][c] = ans
        return ans

    return routes (fuel, start)

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        return count_routes(locations, start, finish, fuel)
