import numpy

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        res = []
        cnt = collections.Counter(''.join(sorted(set(w))) for w in words)
        for p in puzzles:
            bfs = [p[0]]
            for c in p[1:]:
                bfs += [s + c for s in bfs]
            res.append(sum(cnt[''.join(sorted(s))] for s in bfs))
        return res
