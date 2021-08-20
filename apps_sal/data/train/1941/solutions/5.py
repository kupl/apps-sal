from collections import defaultdict


class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ans = [0] * len(puzzles)
        wordSet = {}
        for (i, word) in enumerate(words):
            mask = 0
            for char in word:
                mask |= 1 << ord(char) - ord('a')
            wordSet[mask] = wordSet.get(mask, 0) + 1
        for i in range(len(puzzles)):
            first = 1 << ord(puzzles[i][0]) - ord('a')
            bitSet = 0
            for char in puzzles[i]:
                bitSet |= 1 << ord(char) - ord('a')
            mask = bitSet
            while True:
                if first & mask == first:
                    ans[i] += wordSet.get(mask, 0)
                if mask == 0:
                    break
                mask = mask - 1 & bitSet
        return ans
