from itertools import combinations
from collections import defaultdict


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordmap = defaultdict(int)
        for word in words:
            mask = 0
            for c in word:
                mask = mask | (1 << (ord(c) - ord('a')))
            wordmap[mask] += 1
        ans = [0 for i in range(len(puzzles))]
        for i, p in enumerate(puzzles):
            starting_letter = p[0]
            for k in range(0, len(p[1:]) + 1):
                for comb in combinations(p[1:], k):
                    mask = 1 << (ord(starting_letter) - ord('a'))
                    for c in comb:
                        mask = mask | (1 << (ord(c) - ord('a')))
                    ans[i] += wordmap[mask]
        return ans
