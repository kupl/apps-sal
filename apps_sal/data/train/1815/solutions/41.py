class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        def shift(char, k):
            idx = ord(char) - ord('a')
            return chr(ord('a') + (idx + k) % 26)

        suffix = 0
        ans = []
        for i in range(len(shifts) - 1, -1, -1):
            suffix += shifts[i]
            ans.append(shift(S[i], suffix))
        return ''.join(ans[::-1])
