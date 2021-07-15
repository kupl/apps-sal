class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = {}
        for char in chars:
            if char not in charsDict:
                charsDict[char] = 0
            charsDict[char] += 1
        
        ans = 0
        
        for word in words:
            wordDict = {}
            for char in word:
                if char not in wordDict:
                    wordDict[char] = 0
                wordDict[char] += 1
            
           
            isGood = True
            for key, val in list(wordDict.items()):

                if key not in charsDict:
                    isGood = False
                    break
                elif val > charsDict[key]:
                    isGood = False
                    break                  
            
            if isGood:
                ans += len(word)
            
        
        return ans
        

