class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def countLetter(s):
            res = [0] * 26
            for c in s:
                res[ord(c) - ord('a')] += 1
            return res
        b_count = [0] * 26
        for b in B:
            for (i, c) in enumerate(countLetter(b)):
                b_count[i] = max(b_count[i], c)
        return [x for x in A if all([x >= y for (x, y) in zip(countLetter(x), b_count)])]
