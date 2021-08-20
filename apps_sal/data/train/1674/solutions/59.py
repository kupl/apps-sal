class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        s = 0
        for i in range(len(piles) - 1, -1, -1):
            s += piles[i]
            piles[i] = s

        def bt(m, player, M, remain, spiles):
            if remain <= 0:
                return 0
            key = (player, M, remain)
            if key in m:
                return m[key]
            res = 0
            for take in range(1, 2 * M + 1):
                index = len(piles) - remain
                res = max(res, spiles[index] - bt(m, 1 - player, max(M, take), remain - take, spiles))
            m[key] = res
            return res
        return bt({}, 0, 1, len(piles), piles)
