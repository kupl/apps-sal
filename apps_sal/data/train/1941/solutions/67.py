class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counter = Counter()
        res = []
        for w in words:
            bitmask = 0
            for c in set(w):
                bitmask |= 1 << ord(c)-ord('a')
            counter[bitmask] += 1
            
        for p in puzzles:
            cands = [1<<ord(p[0])-ord('a')]
            for c in p[1:]:
                cands += [b|(1<<ord(c)-ord('a')) for b in cands]

            res.append(sum(counter[b] for b in cands))
            
        return res
            

