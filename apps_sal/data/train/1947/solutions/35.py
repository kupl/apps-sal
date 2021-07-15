class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dic = {}
        out = []
        
        for word in B:
            dicWord = {}
            for letter in word:
                if not letter in dicWord:
                    dicWord[letter] = 1
                else:
                    dicWord[letter] += 1
            for letter in dicWord:
                if not letter in dic:
                    dic[letter] = dicWord[letter]
                else:
                    dic[letter] = max(dic[letter], dicWord[letter])
                    
        for word in A:
            dicWord = {}
            universal = True
            for letter in word:
                if letter in dicWord:
                    dicWord[letter] += 1
                else:
                    dicWord[letter] = 1
            
            for letter in dic:
                if not letter in dicWord:
                    universal = False
                    break
                if dic[letter] > dicWord[letter]:
                    universal = False
                    break                    
                        
            if not universal:
                continue
            else:
                out += [word]
        
        return out
            

