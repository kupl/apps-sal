class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        res = []
        
        count = collections.defaultdict(int)
        for i, w in enumerate(words):
            mask = 0
            for x in w:
                mask |= 1 << (ord(x) - ord('a'))
            count[mask] += 1
            
        for i, p in enumerate(puzzles):
            mask = 0
            for x in p:
                mask |= 1 << (ord(x) - ord('a'))
            
            first = 1 << ord(puzzles[i][0]) - ord('a')
            
            c = 0
            sub = mask
            while True:
                if sub & first == first and sub in count:
                    c += count[sub]
                
                if sub == 0:
                    break
                
                sub = (sub-1)&mask
            res.append(c)
        
        return res
