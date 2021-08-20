class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = collections.Counter()
        for word in words:
            n = 0
            for w in word:
                n = n | 1 << ord(w) - ord('a')
            count[n] += 1
        result = []
        for puzzle in puzzles:
            bfs = [1 << ord(puzzle[0]) - 97]
            m = 0
            for p in puzzle[1:]:
                bfs += [m | 1 << ord(p) - 97 for m in bfs]
            result.append(sum((count[m] for m in bfs)))
        return result
