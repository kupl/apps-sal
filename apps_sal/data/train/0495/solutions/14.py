class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mem = {}  # Mem

        def explore(a, b, stones):
            if len(stones) == 0:
                return abs(a - b)

            entry = (a, b, len(stones))  # Mem
            if entry in mem:
                return mem[entry]

            s = stones.pop()
            m = min(explore(a + s, b, stones), explore(a, b + s, stones))
            stones.append(s)

            mem[entry] = m  # Mem
            return m

        return explore(0, 0, stones)
