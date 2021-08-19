class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        nextS = shifts[0] % 26
        for i in range(len(S)):
            (curr, nextS) = (nextS, shifts[i + 1] % 26 if i < len(S) - 1 else 0)
            shifts[0] += curr if i > 0 else 0
            if i < len(S) - 1:
                shifts[i + 1] = -curr
        for i in range(len(S)):
            shifts[i] += shifts[i - 1] if i > 0 else 0
        return ''.join([chr((ord(c) - 97 + s) % 26 + 97) for (c, s) in zip(S, shifts)])
