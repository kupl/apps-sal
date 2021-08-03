class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        if not A:
            return []
        word_map_B = self.createMapWordB(B)
        res = []

        for word in A:
            if self.searchWord(word, word_map_B):
                res.append(word)
        return res

    def createMapWordB(self, B):
        # Simplify B to be the combination of all letters
        max_B = [0] * 26
        for b in B:
            temp_B = self.createSingleWordCount(b)
            for i in range(26):
                max_B[i] = max(max_B[i], temp_B[i])
        return max_B

    def createSingleWordCount(self, word):
        res = [0] * 26
        for c in word:
            idx = ord(c) - ord('a')
            res[idx] += 1
        return res

    def searchWord(self, word, max_B):
        word_count = self.createSingleWordCount(word)
        for i in range(26):
            if word_count[i] < max_B[i]:
                return False
        return True
