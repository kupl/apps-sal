class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        add = 0
        arr = list(S)
        i = len(S) - 1
        while i >= 0:
            add += shifts[i]
            arr[i] = chr((ord(arr[i]) - 97 + add) % 26 + 97)
            i -= 1
        return ''.join(arr)
