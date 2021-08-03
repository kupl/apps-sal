class Solution:
    def alienCompare(self, word1: str, word2: str, order: str) -> int:
        if word1 == word2:
            return 0
        else:
            i: int = 0
            while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                i += 1
            if i == len(word1):
                return -1
            elif i == len(word2):
                return 1
            elif order.index(word1[i]) < order.index(word2[i]):
                return -1
            else:
                return 1

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n: int = len(words)
        if n == 0 or n == 1:
            return True
        else:
            for i in range(1, n):
                if self.alienCompare(words[i - 1], words[i], order) == 1:
                    return False
            return True
