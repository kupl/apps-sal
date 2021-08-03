class Solution:
    def longestAwesome(self, s: str) -> int:
        last_pos = Counter({0: -1})
        mask = 0

        result = 0
        for i, c in enumerate(s):
            n = int(c)

            mask ^= (1 << n)
            if mask in last_pos:
                result = max(result, i - last_pos[mask])

            for j in range(10):
                new_mask = mask ^ (1 << j)
                if new_mask in last_pos:
                    result = max(result, i - last_pos[new_mask])

            if mask not in last_pos:
                last_pos[mask] = i

        return result
