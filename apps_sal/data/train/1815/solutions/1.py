class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        tot = sum(shifts)
        ans = []
        for i in range(len(S)):
            ans.append(chr((ord(S[i]) - ord('a') + tot) % 26 + ord('a')))
            tot -= shifts[i]
        return ''.join(ans)
