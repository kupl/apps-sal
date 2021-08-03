class Solution:
    def longestAwesome(self, s: str) -> int:
        known_positions = {0: -1}

        mask = 0
        max_size = 0

        for idx, current in enumerate(s):
            mask ^= 1 << (ord(current) - ord('0'))

            for modified in range(10):
                tmp_mask = mask ^ (1 << modified)
                size = idx - known_positions.get(tmp_mask, idx)

                if size % 2:
                    max_size = max(max_size, size)

            max_size = max(max_size, idx - known_positions.get(mask, idx))
            known_positions.setdefault(mask, idx)

        return max(max_size, 1)
