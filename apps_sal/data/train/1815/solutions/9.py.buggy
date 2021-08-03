class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        output = \"\"
        currShift = 0
        for i in range(len(S)-1, -1, -1):
            currShift += shifts[i]
            newPos = (self.getPosition(S[i]) + currShift)%26
            output = self.getLetter(newPos) + output
        return output
        
    def getPosition(self, char):
        return ord(char) - ord('a')
        
    def getLetter(self, position):
        return chr(ord('a') + position)
        
        
