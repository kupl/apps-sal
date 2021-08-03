class Puzzle:
    def __init__(self, puzzle):
        self.first_letter = puzzle[0]
        self.puzzle = set(puzzle)


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = collections.Counter(frozenset(w) for w in words)
        res = [0] * len(puzzles)
        for i, puzzle in enumerate(puzzles):
            for bin_i in range(2**6, 2**7):
                mask = bin(bin_i)[2:]
                subset = frozenset([puzzle[j] for j in range(7) if mask[j] == '1'])
                res[i] += cnt[subset]
        return res
