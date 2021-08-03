class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        total_shifts = [0]
        for s in reversed(shifts):
            total_shifts = [s + total_shifts[0]] + total_shifts
            
        output = \"\"
        for c, shift in zip(S, total_shifts[:-1]):
            output += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        return output
        
