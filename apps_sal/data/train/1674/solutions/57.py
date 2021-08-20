class Solution:

    def stoneGameII(self, piles: List[int]) -> int:

        def stoneGameIIUtil(piles: List[int], m: int, alex: bool) -> int:
            if not piles:
                return 0
            best = 0 if alex else 1000000
            for x in range(1, min(2 * m + 1, len(piles) + 1)):
                total = sum(piles[:x]) if alex else 0
                total += stoneGameIIUtil(piles[x:], max(m, x), not alex)
                best = max(best, total) if alex else min(best, total)
            return best
        return stoneGameIIUtil(piles, 1, True)

    def stoneGameII(self, piles: List[int]) -> int:
        lookup = {}

        def stoneGameIIUtil(piles: List[int], m: int, alex: bool) -> int:
            if not piles:
                return 0
            if (tuple(piles), m, alex) in lookup:
                return lookup[tuple(piles), m, alex]
            best = 0 if alex else 1000000
            for x in range(1, min(2 * m + 1, len(piles) + 1)):
                total = sum(piles[:x]) if alex else 0
                total += stoneGameIIUtil(piles[x:], max(m, x), not alex)
                best = max(best, total) if alex else min(best, total)
            lookup[piles, m, alex] = best
            return best
        return stoneGameIIUtil(tuple(piles), 1, True)
