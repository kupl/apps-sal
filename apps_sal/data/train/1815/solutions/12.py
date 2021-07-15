class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        def shift(s, n):
            curr = ord(s)-97
            curr = 97 + (curr+n)%26
            return chr(curr)
        S = list(S)
        shifts = shifts[::-1]
        for i in range(1, len(shifts)):
            shifts[i] += shifts[i-1]
        shifts = shifts[::-1]
        
        for i in range(len(shifts)):
            S[i] = shift(S[i], shifts[i])
        return ''.join(S)
