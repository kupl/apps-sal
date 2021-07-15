class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsums = 0
        chars = sorted(chars)
        
        for word in words:
            wordsize = len(word)
            word = sorted(word)
            charcounter = 0
            
            while len(word) > 0 and charcounter < len(chars):
                if word[0] == chars[charcounter]:
                    word.remove(word[0])
                    charcounter += 1
                else:
                    charcounter += 1
            
            if len(word) == 0:
                charsums += wordsize
        
        return charsums
