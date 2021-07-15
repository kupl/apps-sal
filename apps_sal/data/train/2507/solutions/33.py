class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        
        ans = 0
        
        for word in words:
            charscopy = [i for i in chars]
            count = 0
            for char in word:
                if char in charscopy:
                    count+=1
                    charscopy.remove(char)
            if count==len(word):
                ans+=len(word)
                
        return ans
