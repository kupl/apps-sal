class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def count(word):
            result = [0] * 26
            for letter in word:
                result[ord(letter) - ord('a')] += 1
            return result
        bmax = [0] * 26
        for b in B:
            for (i, c) in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        result = []
        for a in A:
            if all((x >= y for (x, y) in zip(count(a), bmax))):
                result.append(a)
        return result
