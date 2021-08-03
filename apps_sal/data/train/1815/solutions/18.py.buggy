class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        x = sum(shifts)
        ans = []
        for i, s in enumerate(S):
            idx = ord(s)- ord('a')
            ans.append(chr(ord('a')+(idx+x)%26))
            x-=shifts[i]
        return \"\".join(ans)
            
