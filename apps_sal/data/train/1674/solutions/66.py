class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def pick_stones(i, m, t):
            '''
            m -> player can pick 1<=X<=2M piles
            t -> player 1's turn if true else 0
            '''
            if i >= len(piles):
                return 0
            if (i, m, t) in d:
                return d[(i, m, t)]
            if t:
                d[(i, m, t)] = max(pick_stones(i + k, max(m, k), 1 - t) + sum(piles[i:i + k]) for k in range(1, 2 * m + 1))
            else:
                d[(i, m, t)] = min(pick_stones(i + k, max(m, k), 1 - t) for k in range(1, 2 * m + 1))
            return d[(i, m, t)]
        d = {}
        return pick_stones(0, 1, True)
