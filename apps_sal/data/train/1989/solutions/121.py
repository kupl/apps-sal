class Solution:
    def longestAwesome(self, s: str) -> int:
        max_len = 0
        mapping_pos = {0: -1}
        acc = 0

        for idx, digit in enumerate([ord(c) - ord('0') for c in s]):
            acc ^= (1 << digit)

            # all possible palindromes have 0 ones or one 1 in either position
            for x in range(10):
                tmp = acc ^ (1 << x)

                if tmp in mapping_pos:
                    max_len = max(max_len, idx - mapping_pos[tmp])

            if acc in mapping_pos:
                max_len = max(max_len, idx - mapping_pos[acc])

            if acc not in mapping_pos:
                mapping_pos[acc] = idx

        return max_len
