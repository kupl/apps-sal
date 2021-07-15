class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordMap = {}
        for word in words:
            encode = 0
            for char in word:
                encode |= 1<<(ord(char)-ord(\"a\"))
            wordMap[encode] = wordMap.get(encode, 0)+1
            
        
        wordCount = []
        for puzzle in puzzles:
            mask = 0
            for char in puzzle:
                mask |= 1<<(ord(char)-ord(\"a\"))
                
            substring = mask

            first = 1<<ord(puzzle[0])-ord(\"a\")
            count = 0
            while substring:
                if (first&substring)==first and substring in wordMap:
                    count += wordMap[substring]
                    
                substring = (substring-1)&mask
                
            wordCount.append(count)
            
        return wordCount
                    
                
                
            
            
                                
