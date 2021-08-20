class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        mem = {}

        def explore(a, b, stones):
            if len(stones) == 0:
                return abs(a - b)
            entry = (a, b, len(stones))
            if entry in mem:
                return mem[entry]
            s = stones.pop()
            m = min(explore(a + s, b, stones), explore(a, b + s, stones))
            stones.append(s)
            mem[entry] = m
            return m
        return explore(0, 0, stones)

    def lastStoneWeightIITLE(self, stones: List[int]) -> int:
        N = len(stones)
        if not stones:
            return 0
        if N == 1:
            return stones[0]
        if N == 2:
            return abs(stones[0] - stones[1])
        out = float('inf')
        for i in range(N):
            for j in range(i + 1, N):
                right = stones.pop(j)
                left = stones.pop(i)
                diff = abs(right - left)
                out = min(out, self.lastStoneWeightII(stones + [diff]))
                stones.insert(i, left)
                stones.insert(j, right)
        return out
