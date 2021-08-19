class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = collections.Counter()
        for w in words:
            if len(set(w)) > 7:
                continue
            m = 0
            for c in w:
                m |= 1 << ord(c) - ord('a')
            count[m] += 1
        res = []
        for p in puzzles:
            bfs = [1 << ord(p[0]) - ord('a')]
            for c in p[1:]:
                bfs += [m | 1 << ord(c) - ord('a') for m in bfs]
            m = 0
            for i in bfs:
                m += count[i]
            res.append(m)
        return res
