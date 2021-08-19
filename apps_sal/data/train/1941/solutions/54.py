class Puzzle:

    def __init__(self, puzzle):
        self.first_letter = puzzle[0]
        self.puzzle = set(puzzle)


class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = collections.Counter((frozenset(w) for w in words))
        res = [0] * len(puzzles)
        for (i, puzzle) in enumerate(puzzles):
            subsets = [puzzle[0]]
            for c in puzzle[1:]:
                subsets += [sub + c for sub in subsets]
            res[i] += sum((cnt[frozenset(sub)] for sub in subsets))
        return res
