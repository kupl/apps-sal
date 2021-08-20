class Solution:

    def longestAwesome(self, s: str) -> int:
        digits = [2 ** i for i in range(10)] + [0]
        (max_len, xor, dictF, dictB) = (0, 0, {0: -1}, {})
        for i in range(len(s)):
            xor = xor ^ digits[int(s[i])]
            if xor not in dictF:
                dictF[xor] = i
            dictB[xor] = i
        max_len = 0
        for i in dictB:
            max_len = max([max_len] + [dictB[i] - dictF[j ^ i] for j in digits if j ^ i in dictF])
        return max_len
