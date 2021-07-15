class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = collections.Counter()
        
        for word in words:
            m = 0
            for c in word:
                m |= 1 << (ord(c) - 97)
            count[m] += 1
            
        res = []
        for puzzle in puzzles:
            bfs = [1 << (ord(puzzle[0]) - 97)]
            
            for c in puzzle[1:]:
                bfs += [x | (1 << (ord(c)-97) )for x in bfs]
                
            res.append(sum(count[x] for x in bfs))
            
        return res
