class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordPatternCnt = collections.defaultdict(int)
        
        for word in words:
            pattern = 0
            for letter in word:
                pattern |= (1 << ord(letter) - ord(\"a\"))
            wordPatternCnt[pattern] += 1
        
        res = []
        
        for puzzle in puzzles:
            cnt = 0
            pattern = 0
            for letter in puzzle:
                pattern |= (1 << (ord(letter) - ord(\"a\")))
                
            subPattern = pattern
                
            while subPattern > 0:
                if subPattern & (1 << (ord(puzzle[0]) - ord(\"a\"))): #valid pattern must conclude the first letter of puzzle
                    cnt += wordPatternCnt[subPattern]
                    
                subPattern = pattern & (subPattern - 1)
            
            res.append(cnt)
        
        return res
                
