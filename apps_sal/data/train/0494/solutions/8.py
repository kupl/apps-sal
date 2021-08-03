class Solution:
    def longestDecomposition(self, text: str) -> int:
        l, r, lh, rh, curr_len, modulo, base, res = 0, len(text) - 1, 0, 0, 0, 32416189573, 26, 0
        nums = [ord(c) - ord('a') for c in text]
        while l < r:
            lh = (lh * base + nums[l]) % modulo
            rh = (nums[r] * base**curr_len + rh) % modulo
            curr_len += 1

            if lh == rh and text[l - curr_len + 1:l + 1] == text[r:r + curr_len]:
                res += 2
                lh = rh = curr_len = 0
            l += 1
            r -= 1

        if l == r or curr_len:
            res += 1

        return res
