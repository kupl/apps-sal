class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        N, ans = 40000, 0
        freq, free_slot = [0] * N, 0
        for n in A:
            freq[n] += 1
        for i, r in enumerate(freq):
            if r:
                ans += (r * (r - 1)) // 2 + (free_slot - i) * r
                free_slot += r
            else:
                free_slot = max(free_slot, i + 1)
        return ans
