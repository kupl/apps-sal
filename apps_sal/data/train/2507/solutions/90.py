class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c1 = [0] * 256
        for c in chars:
            c1[ord(c)] += 1
            
        res = 0
        for word in words:
            c2 = [0] * 256
            for c in word:
                c2[ord(c)] += 1
            
            goodStr = True
            for i in range(256):
                if c1[i] < c2[i]:
                    goodStr = False
                    break
            
            if goodStr:
                res += len(word)
        return res
