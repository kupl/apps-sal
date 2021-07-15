class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        res = []
        
        counter = collections.defaultdict(int)
        
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            
            counter[mask] += 1
        
        for puzzle in puzzles:
            mask = 0
            for c in puzzle:
                mask |= 1 << (ord(c) - ord('a'))
            
            first = 1 << (ord(puzzle[0]) - ord('a'))
            
            c = 0
            sub = mask
            
            while True:
                if sub & first == first and sub in counter:
                    c += counter[sub]
                
                if sub == 0:
                    break
                    
                sub = (sub-1)&mask
            
            res.append(c)
        return res
