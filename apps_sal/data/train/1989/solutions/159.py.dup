class Solution:
    def longestAwesome(self, s: str) -> int:
        known_positions = {0: 0}

        mask = 0
        max_size = 0

        for idx, current in enumerate(s):
            mask ^= 1 << (ord(current) - ord('0'))

            for modified in range(10):
                tmp_mask = mask ^ (1 << modified)

                if tmp_mask in known_positions:
                    size = idx - known_positions[tmp_mask] + 1

                    if size % 2:
                        max_size = max(max_size, size)

            if mask in known_positions:
                max_size = max(max_size, idx - known_positions[mask] + 1)

            else:
                known_positions[mask] = idx + 1

        return max(max_size, 1)
